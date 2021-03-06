#!/usr/bin/python
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab


import ez_setup
ez_setup.use_setuptools()

import sys, os
from glob import glob
from setuptools import setup, find_packages

NAME = "pycopia-WWW"
VERSION = "1.0a4"

DNAME = NAME.split("-", 1)[-1]
ENAME = NAME.replace("-", "_")

setup (name=NAME, version=VERSION,
    namespace_packages = ["pycopia"],
    packages = find_packages(),
    install_requires = ['pycopia-XML>=1.0a1,==dev', 'simplejson>=0.7'],
    data_files = [
        ('/etc/pycopia', glob("etc/*.example") + glob("etc/*.dist")),
        ('/etc/pycopia/lighttpd', glob("etc/lighttpd/*")),
        (os.path.join(sys.prefix, 'share', 'pycopia', 'docs', 'html'), 
             glob("doc/html/*.html")),
        (os.path.join(sys.prefix, 'share', 'pycopia', 'docs', 'html', 'cgi-bin'), 
             glob("doc/html/cgi-bin/*.py")),
        (os.path.join(sys.prefix, 'share', 'pycopia', 'media', 'js'), 
             glob("media/js/*.js")),
        (os.path.join(sys.prefix, 'libexec', 'pycopia'), glob("libexec/*")),
    ],
    scripts = glob("bin/*"), 
    test_suite = "test.WWWTests",

    description = "Pycopia WWW tools and web application framework.",
    long_description = """Pycopia WWW tools and web application framework.
    Provides FCGI servers, XHTML page generator with functional style
    interfaces, XHTML generator objects, and lightweight web application
    framework. Some support for WML as well. Designed to work closely with
    the lighttd front-end server via the FCGI interface. You may run any
    number of FCGI handlers, each in its own process with its own user ID
    and associated permissions. Generally, supports a design comprised of
    a set of JSON handlers with the expectation that the web application
    will be mostly provided by Javascript on the client side.  The
    framework also works with Google's web application engine.""",
    license = "LGPL",
    author = "Keith Dart",
    author_email = "keith@kdart.com",
    keywords = "pycopia WWW framework XHTML FCGI WSGI",
    url = "http://www.pycopia.net/",
    download_url = "http://pycopia.googlecode.com/svn/trunk/%s#egg=%s-dev" % (DNAME, ENAME),
    #download_url = "ftp://ftp.pycopia.net/pub/python/%s.%s.tar.gz" % (NAME, VERSION),
    classifiers = ["Operating System :: POSIX", 
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
                   "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
                   "Topic :: Software Development :: Quality Assurance",
                   "Intended Audience :: Developers"],
)

