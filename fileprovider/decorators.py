from functools import wraps

from django.http import HttpResponse

def file_response(func):
    @wraps(func)
    def provider_response(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, basestring):
           response = HttpResponse()
           response['X-File'] = result
        return response
    return provider_response


def file_response_cached(func):
    @wraps(func)
    def provider_response(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, basestring):
           response = HttpResponse()
           response['X-File'] = result
        return response
    return provider_response

