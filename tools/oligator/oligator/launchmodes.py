#!/usr/bin/env python
#
# launchmodes.py
#
# $Log: launchmodes.py,v $
# Revision 1.1.2.1  2003/04/16 18:19:43  nadya
# Multiple changes to incorporate Postgres as an alternative to MySQL
#
#

###############################################################
# launch Python programs with reusable launcher scheme classes;
# assumes 'python' is on your system path (but see Launcher.py)
###############################################################

import os
import string
# import sys

pycmd = 'python'   # assume it is on your system path


class LaunchMode:
    def __init__(self, label, command):
        self.what = label
        self.where = command

    def __call__(self):                   # on call, ex: button press callback
        self.announce(self.what)
        self.run(self.where)              # subclasses must define run()

    def announce(self, text):             # subclasses may redefine announce()
        print(text)                        # methods instead of if/elif logic

    def run(self, cmdline):
        assert 0, 'run must be defined'


class System(LaunchMode):                          # run shell commands
    def run(self, cmdline):                        # caveat: blocks caller
        os.system('%s %s' % (pycmd, cmdline))      # unless '&' added on Linux


class Popen(LaunchMode):                           # caveat: blocks caller
    def run(self, cmdline):                        # since pipe closed too soon
        os.popen(pycmd + ' ' + cmdline)            # 1.5.2 fails in Windows GUI


class Fork(LaunchMode):
    def run(self, cmdline):
        assert hasattr(os, 'fork')                 # for linux/unix today
        cmdline = string.split(cmdline)            # convert string to list
        if os.fork() == 0:                         # start new child process
            os.execvp(pycmd, [pycmd] + cmdline)    # run new program in child


class Top_level(LaunchMode):
    def run(self, cmdline):                          # new window, same process
        # tbd: need GUI class info
        assert 0, 'Sorry - mode not yet implemented'


# if sys.platform[:3] == 'win':
#     PortableLauncher = Spawn            # pick best launcher for platform
# else:                                   # need to tweak this code elsewhere
PortableLauncher = Fork


class QuietPortableLauncher(PortableLauncher):
    def announce(self, text):
        pass


def selftest():
    myfile = 'launchmodes.py'
    program = 'textEditor.py ' + myfile       # assume in cwd
    input('default mode...')  # raw_input in python 2
    launcher = PortableLauncher('PyEdit', program)
    launcher()                                                # no block

    input('system mode...')
    System('PyEdit', program)()                               # blocks

    input('popen mode...')
    Popen('PyEdit', program)()                                # blocks

#    if sys.platform[:3] == 'win':
#        raw_input('DOS start mode...')                        # no block
#        Start('PyEdit', program)()


if __name__ == '__main__':
    selftest()
