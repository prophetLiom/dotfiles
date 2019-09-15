#! /usr/bin/python

import subprocess

partition = '/'
df = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)

for line in df.stdout:
    splitline = line.decode().split()
    if splitline[5] == partition:
        print(' ' + splitline[3] + ' of ' + splitline[1] + ' left (' + splitline[4] + ' used)')
