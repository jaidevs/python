#!/usr/bin/python
import shutil, os, sys, os.path
print '''\n Note : Will Delete Directory and its Contents Recursively \n'''
path =  raw_input("Enter path to be removed : ")
def delete_folder():
    if not os.path.exists(path):
       print "folder doesnt exist"
    else:
       shutil.rmtree(path)
       print "folder is removed"

delete_folder()



# age = input("What is your age? ")
# to get integer
