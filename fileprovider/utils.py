from django.http import HttpResponse

def sendfile(path):
    response = HttpResponse()
    response['X-File'] = path
    return response
