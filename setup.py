from setuptools import setup

__version__  = '0.1a3'

setup(
    name='django-fileprovider',
    version=__version__,
    description='django middleware for serving media files',
    author='Renjith Thankachan',
    author_email='mail3renjith@gmail.com',
    url='https://bitbucket.org/renlinx007/django-file-provider',
    download_url='https://bitbucket.org/renlinx007/django-fileprovider/get/0.1a3.tar.gz',
    long_description=open('README.md', 'r').read(),
    packages=[
        'fileprovider',
    ],
    zip_safe=False,
    requires=[
    ],
    install_requires=[
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
