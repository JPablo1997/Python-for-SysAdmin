#!/usr/bin/env python

import subprocess
import sys

#Codigo para traducir texto en ingles a texto en español y con su respectiva pronunciación en ingles

en_text = sys.argv[1]

subprocess.call("trans -b -sp :es en: '%s'" % en_text, shell=True)