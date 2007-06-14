#!/usr/bin/python2.4
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab


import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, Extension 

NAME = "pycopia-XXX"
DNAME = NAME.split("-", 1)[-1]
VERSION = "1.0"

setup (name=NAME, version=VERSION,
#    ext_modules = [_XXX],
#    py_modules = ["XXX"],
    namespace_packages = ["pycopia"],
    packages = ["pycopia"],
    install_requires = ['pycopia-aid>=1.0a1,==dev'],
    test_suite = "test.XXXTests",

    description = "",
    long_description = """
    """,
    license = "LGPL",
    author = "Keith Dart",
    author_email = "keith@kdart.com",
    keywords = "pycopia framework",
    url = "http://www.pycopia.net/",
    download_url = "http://pycopia.googlecode.com/svn/trunk/%s#egg=%s-dev" % (DNAME, NAME),
    #download_url = "ftp://ftp.pycopia.net/pub/python/%s.%s.tar.gz" % (NAME, VERSION),
    classifiers = ["Operating System :: POSIX", 
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Topic :: System :: Networking :: Monitoring",
                   "Intended Audience :: Developers"],
)


