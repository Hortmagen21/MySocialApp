from django.utils import timezone
from .models import Profile


def is_restricted_internal_url(url):
    URL_PREFIXES_EXCLUDES = [
        '/admin/',
        '/login/',
        '/register/',
    ]
    return not max([url.startswith(x) for x in URL_PREFIXES_EXCLUDES])


def update_last_activity_middleware(get_response):
    def middleware(request):
        assert hasattr(request, 'user')
        if request.user.is_authenticated:
            Profile.objects.filter(user__id=request.user.id) \
                           .update(last_activity=timezone.now())
        response = get_response(request)
        return response
    return middleware


