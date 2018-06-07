#!/usr/bin/python
import shutil, os, os.path, sys
print "\n will delete a file or a directory recursively. \n"
path =  raw_input("Enter path to be removed : ")
def delete_file():
    if not os.path.isfile(path):
       print "file doesnt exist"
    else:
       os.remove(path)
       print "file is removed"


def delete_folder():
    if not os.path.exists(path):
       print "folder doesnt exist"
    else:
       shutil.rmtree(path)
       print "folder is removed"

if os.path.exists(path):
    delete_folder()

else os.path.isfile(path):
    delete_file()
