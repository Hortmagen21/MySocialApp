from django.db import IntegrityError
from rest_framework.views import Response, exception_handler
from rest_framework import status


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if isinstance(exc, IntegrityError) and not response:
        response = Response(
            {
                'message': "The same User can't like the same post twice"
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    return response

