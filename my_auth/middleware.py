from rest_framework_simplejwt.exceptions import InvalidToken

from .models import Profile
from django.utils import timezone
from rest_framework_simplejwt import authentication


def is_restricted_internal_url(url):
    URL_PREFIXES_EXCLUDES = [
        '/login/',
        '/register/',
        '/admin/',
    ]
    return not max([url.startswith(x) for x in URL_PREFIXES_EXCLUDES])


def update_last_activity_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        if is_restricted_internal_url(request.path_info):
            try:
                request.user = authentication.JWTAuthentication().authenticate(request)[0]
            except InvalidToken:
                return response
        if request.user.is_authenticated:
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


