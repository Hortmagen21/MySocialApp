from .models import Profile
from django.utils import timezone


def update_last_activity_middleware(get_response):
    def middleware(request):
        response = get_response(request)

        if request.user.is_authenticated and request.path_info != '/info/':
            Profile.objects.filter(user__id=request.user.id) \
                           .update(last_activity=timezone.now())
            '''
              P.S.
              Probably sometimes such data should be placed in cache
              rather than create plethora of db connections,
              but because it doesn't seem like testing task will have a lot of connections
              i neglected that thread  
            '''
        return response
    return middleware


