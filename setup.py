from setuptools import setup

__version__  = '0.1.3'
 
setup(
    name='django-fileprovider',
    version=__version__,
    description='django middleware for serving media files ( or protect them )',
    author='Renjith Thankachan',
    author_email='mail3renjith@gmail.com',
    url='https://github.com/instapk/django-fileprovider.git',
    download_url='https://github.com/instapk/django-fileprovider/archive/0.1.3.tar.gz',
    long_description=open('README.md', 'r').read(),
    packages=[
        'fileprovider',
    ],
    zip_safe=False,
    requires=[
    ],
    install_requires=[
      'six>=1.10.0',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Utilities'
    ],
)
