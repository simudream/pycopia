#!/usr/bin/python
# vim:ts=4:sw=4:softtabstop=0:smarttab
# 
#    Copyright (C) 1999-2007  Keith Dart <keith@kdart.com>
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.

"""
Master builder (custom script).

Commands:
 sdist
 publish
 build
 install
 develop
 list

NOTE: install requires sudo to be configured for you.

"""

import sys
import os


PACKAGES = [
"aid",
"utils",
"core",
"CLI",
"debugger",
"process",
"SMI",
"mibs",
"SNMP",
"storage",
"QA",
"net",
"audio",
"XML",
"WWW",
"vim",
]

SQUASHDIR = "/var/tmp/python"

def _do_commands(name, cmds, root):
    if root:
        sudo = "sudo "
    else:
        sudo = ""
    cmd = "%s%s setup.py %s" % (sudo, sys.executable, " ".join(cmds))
    print "========", name, "==", cmd
    os.chdir(name)
    try:
        os.system(cmd)
    finally:
        os.chdir("..")
        print "====================== END", name
        print

def do_sdist(name):
    _do_commands(name, ["sdist"], False)

def do_build(name):
    _do_commands(name, ["build"], False)

def do_list(name):
    print name,

#def do_register(name):
#    _do_commands(name, ["register"], False)

def do_develop(name):
    _do_commands(name, ["develop -s $HOME/bin"], False)

def do_publish(name):
    _do_commands(name, ['egg_info -RDb ""', "sdist", "register", "upload"], False)

def do_egg_info(name):
    _do_commands(name, ['egg_info'], False)

def do_install(name):
    _do_commands(name, ["install"], True)

# "squash" selected sub packages to a single package. Also removes
# setuptools dependency when tarballed.
def do_squash(name):
    if not os.path.isdir(SQUASHDIR):
        os.mkdir(SQUASHDIR)
    #_do_commands(name, ["build"], False)
    os.chdir(name)
    uname = os.uname()
    bin_dir = "build/lib.%s-%s-%s" % (uname[0].lower(), uname[4], sys.version[:3])
    # e.g: build/lib.linux-x86_64-2.5/pycopia
    print "======== SQUASH", name, "to", SQUASHDIR
    try:
        os.system("%s setup.py build" % (sys.executable,))
        for pydir in ("build/lib", bin_dir):
            if os.path.isdir(pydir):
                cmd = "rsync -azvu %s/ %s" % (pydir, SQUASHDIR)
                os.system(cmd)
    finally:
        os.chdir("..")
    _null_init(SQUASHDIR)
    print "====================== END", name
    print

def _null_init(directory):
    open(os.path.join(directory, "pycopia", "__init__.py"), "w").close()




def main(argv):
    try:
        cmd = argv[1]
    except IndexError:
        print __doc__
        return 1
    try:
        meth = globals()["do_" + cmd]
    except KeyError:
        print __doc__
        return 2
    for name in (argv[2:] or PACKAGES):
        meth(name)
    print
    return 0

sys.exit(main(sys.argv))
