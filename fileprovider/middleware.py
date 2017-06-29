import os
import six

from django.conf import settings
from django.core.files.base import File
from django.http import HttpResponse, HttpResponseNotFound, FileResponse

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

class FileProvider(object):
      def get_response(self, response, **options):
          return self._get_response(response, **options)

      def _get_response(self, response, **options):
          raise NotImplemented

class XAccelFileProvider(FileProvider):
      def _get_response(self, response, **options):
          response['X-Accel-Redirect'] = response['X-File']
          del response['X-File']
          return response

class XSendFileProvider(FileProvider):
      def _get_response(self, response, **options):
          response['X-Sendfile'] = response['X-File']
          del response['X-File']
          return response

class PythonFileProvider(FileProvider):
      def _get_response(self, response, **options):
          # only need this checking when python file provider is given
          if not os.path.exists(response['X-File']):
              return HttpResponseNotFound("file not found")
          return FileResponse(open(response['X-File'], 'rb'))

# Uses X-Sendfile
ApacheFileProvider = XSendFileProvider
LightHttpdFileProvider = XSendFileProvider
HiawathaFileProvider = XSendFileProvider
# Uses X-Accel-Redirect
NginxFileProvider = XAccelFileProvider
CaddyFileProvider = XAccelFileProvider

PROVIDERS = {
 'python': PythonFileProvider,
 'nginx': NginxFileProvider,
 'apache': ApacheFileProvider,
 'lighthttpd': LightHttpdFileProvider,
 'caddy': CaddyFileProvider,
 'hiawatha': HiawathaFileProvider,
 'xaccel': XAccelFileProvider,
 'xsendfile': XSendFileProvider,
}

class FileProviderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        filepath = response.get('X-File', "")
        if filepath != "" and isinstance(filepath, six.string_types):
            provider_name = getattr(settings, "FILEPROVIDER_NAME", "python")
            # provider_option = getattr(settings, "DJM_ENABLE_CACHE", True)
            provider = PROVIDERS[provider_name]
            response =  provider().get_response(response)
        return response
