#!/usr/bin/python
import os, os.path, sys
path = raw_input("Enter filename to be removed with absolute path: ")
def delete_file():
   if not os.path.isfile(path):
    print "file doesnt exist"
   else:
    os.remove(path)
    print "file is removed"

delete_file()

# age = input("What is your age? ")
# to get integer
