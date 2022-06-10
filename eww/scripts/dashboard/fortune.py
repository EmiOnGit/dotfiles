#!/bin/python

import subprocess

quote=subprocess.run('fortune', capture_output=True, text=True).stdout
while len(quote.split('\n')) > 3:
    quote=subprocess.run('fortune', capture_output=True, text=True).stdout
print(quote)