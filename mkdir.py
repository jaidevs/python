#!/usr/bin/python

import os, sys, os.path

# Path to be created
path = "/tmp/jaidev"
#new = "king"
if not os.path.exists(path):
   os.mkdir( path, 0755 )
   print "Path is created"
else:
 print "Folder already exist"





#os.chdir(path)
#os.mkdir( new, 0755 );
