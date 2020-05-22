#!/usr/bin/env python

import subprocess

command = "echo test"

subprocess.Popen(command, shell=True)