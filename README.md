[![Downloads](https://pypip.in/download/django-fileprovider/badge.svg)](https://pypi.python.org/pypi/django-fileprovider/)

File handler for django, useful when you want to add control or logic to served files.  
It uses `sendfile` API supports on different servers and uses pythonic solution on django development server.  
Currently it supports,  

* Apache  
* Nginx  
* LightHttpd  
* Caddy  
* Proxygen   
* H2O/Reproxy  
* Hiawatha  

# INSTALLATION  

  use pip to install package:  
  `pip install django-fileprovider`  

   NOTE: if you are installing from github version consider checking [releases](https://github.com/sideffect0/django-fileprovider/releases)

* add `fileprovider` to django `INSTALLED_APPS` section.  
* add `fileprovider.middleware.FileProviderMiddleware` to `MIDDLEWARE_CLASSES` section
* set django `settings` file with `FILEPROVIDER_NAME` any of  available providers `python`, `nginx`, `apache`, `lighthttpd`, 
`caddy`, `hiawatha`, `xsendfile`, `xaccel`.  

 ```python  
    
    # or you can put FILEPROVIDER_NAME as python in your local settings file  
    if settings.DEBUG:
        FILEPROVIDER_NAME = "python"
    else:
        # or apache, lighthttpd, caddy
        FILEPROVIDER_NAME = "nginx"

 ```

# USAGE  

 on django views where file response is required, fill response header `X-File` with absolute file path or use `sendfile` wrapper    
 for example,  

 ```python  

    from fileprovider.utils import sendfile  
    def hello(request):
        return sendfile('/absolute/path/to/file')

    # can be used protecting file access from unauthorized users
    @login_required
    def hello(request, file_id):
        file = get_object_or_404(FileModel, pk=file_id)
        return sendfile(file.path)

 ```
