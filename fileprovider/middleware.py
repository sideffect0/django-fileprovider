import os

from django.conf import settings
from django.core.files.base import File
from django.http import HttpResponse, HttpResponseNotFound
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

class FileProvider(object):
      def get_response(self, response, **options):
          return self._get_response(response, **options)

      def _get_response(self, response, **options):
          raise NotImplemented

class NginxFileProvider(FileProvider):
      def _get_response(self, response, **options):
          response['X-Accel-Redirect'] = response['X-File']
          return response

class ApacheFileProvider(FileProvider):
      def _get_response(self, response, **options):
          response['X-Sendfile'] = response['X-File']
          return response

class PythonFileProvider(FileProvider):
      def _get_response(self, response, **options):
          # only need this checking when python file provider is given
          if os.path.exists(response['X-File']):
              return HttpResponseNotFound("file not found")
          with File(open(response['X-File'], 'rb')) as f:
              response =  HttpResponse(f.chunks()) 
          return response

# Uses lighthttpd X-Sendfile
LightHttpdFileProvider = ApacheFileProvider
# Uses X-Accel-Redirect
CaddyFileProvider = NginxFileProvider

PROVIDERS = {
 'python': PythonFileProvider,
 'nginx': NginxFileProvider,
 'apache': ApacheFileProvider,
 'lighthttpd': LightHttpdFileProvider,
 'caddy': CaddyFileProvider,
}

class FileProviderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.get('X-File', "") != "":
            provider_name = getattr(settings, "FILEPROVIDER_NAME", "python")
            # provider_option = getattr(settings, "DJM_ENABLE_CACHE", True)
            provider = PROVIDERS[provider_name]
            response =  provider().get_response(response)
        return response
