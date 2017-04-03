[![Build Status](https://travis-ci.org/instapk/django-fileprovider.svg?branch=master)](https://travis-ci.org/instapk/django-fileprovider)  

File handler for django, useful when you want to add control or logic to served files.  
It uses `sendfile` supports on different servers and uses pythonic solution on django development server.  
Currently it supports,  

* Apache  
* Nginx  
* LightHttpd  
* Caddy  
* Hiawatha  

# INSTALLATION  

  use pip to install package:  
  `pip install django-fileprovider`  

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

 on django views where file response is required, fill response header `X-File` with absolute file path  
 for example,  

 ```python  
      
    def hello(request):
        response = HttpResponse()
        response['X-File'] = '/absolute/path/to/file'
        return response
 ```
