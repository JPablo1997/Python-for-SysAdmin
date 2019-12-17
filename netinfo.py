#!/usr/bin/env python

import subprocess

def getIntIP():
    return subprocess.call('echo "Internal IP: $(hostname -I)"', shell=True)

def getExtIP():
    return subprocess.call('echo "External IP: $(curl -s http://ifconfig.me)"', shell=True)

def main():
    getIntIP()
    getExtIP()

main()
