
#!/usr/bin/python3

# add library imports
import sys
import re
import zipfile
from datetime import datetime
import pickle
print("hello world")

# global variables:
counts = {'fic':{}, 'news':{}, 'spok':{}, 'tvm':{}}
verbs = {}

def read_verbs(filename):
  # read and load verbs:
  with open(filename) as f: 
    for line in f:
      line = line.strip()
      parts = line.split(" ")
      verbs[parts[0]] = parts
  # setup counts directories:
  for v in verbs.keys():
    counts['fic'][v]=[]
    counts['news'][v]=[]
    counts['spok'][v]=[]
    counts['tvm'][v]=[]

# more info:
# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
