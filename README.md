File handler for django, useful when you want to add control or logic to served files.  
It uses `sendfile` supports on different servers and uses pythonic solution on django development server.  
Currently it supports,  

* Apache  
* Nginx  
* LightHttpd  
* Caddy  

# INSTALLATION  

  use pip to install package:  
  `pip install -e git+https://github.com/instapk/django-fileprovider.git@0.1#egg=django-fileprovider`  

* add `fileprovider` to django `INSTALLED_APPS` section.  
* add `fileprovider.middleware.FileProviderMiddleware` to `MIDDLEWARE_CLASSES` section
* set django `settings` file with `FILEPROVIDER_NAME` any of  available providers {'python', 'nginx', 'apache', 'lighthttpd', 'caddy', }

# USAGE  

 on django views where file response is required, fill response header `X-File` with absolute file path  
 for example,  

 ```python  
      
    def hello(request):
        response = HttpResponse()
        response['X-File'] = '/absolute/path/to/file'
        return response
 ```
