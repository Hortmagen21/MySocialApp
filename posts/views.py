from django.db.models import Count
from rest_framework.generics import GenericAPIView
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer, LikeByDaySerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters


class PostCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikePost(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DisLikePost(mixins.DestroyModelMixin, GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    lookup_field = 'post'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg],
                         "author": self.request.user.pk}
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class LikeFilter(filters.FilterSet):
    date_from = filters.DateTimeFilter(field_name='liked_on', lookup_expr='gte')
    date_to = filters.DateTimeFilter(field_name='liked_on', lookup_expr='lte')

    class Meta:
        model = Like
        fields = ['liked_on']


class LikeList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeByDaySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LikeFilter

    def get_queryset(self):
        return Like.objects.extra(select={'date': "date(posts_like.liked_on)"}).values("date") \
            .annotate(likes=Count('pk'))





