#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import walk
from os.path import join
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("purpose")
parser.add_argument("-p", "--path", help="define the path of Darknet")
parser.add_argument("-r", "--range", help="define the range of directory(n-m) used for the image list")
args = parser.parse_args()
aim = args.purpose
if args.range:
    range = args.range.split("-")
    print("from " + range[0] + " to " + range[1])
fileType = ".jpg"

if args.path:
    path = args.path
    outFilePath = join(path, aim + ".txt")
else:
    darknetPath = "D:\\UnityProjectPackages\Object_Detection_yolo\darknet\\build\darknet\\x64\\"
    path = join(darknetPath, "data\obj")
    outFilePath = darknetPath + "data\\" + aim + ".txt"

fp = open(outFilePath, "w")

for root, dirs, files in walk(path):
    parts = root.split("\\")
    index = parts.index("data")
    catPath = ""
    if args.range:
        if(not parts[-1].isnumeric()):
            continue
        dIndex = int(parts[-1]) #folder index
        if(dIndex < int(range[0]) or dIndex > int(range[1])):
            continue
    print("Adding directory " + parts[-1])
    for p in parts[index:]:
        catPath = join(catPath, p)
    for f in files:
        if f == "classes.txt":
            continue
        sub = f.split(".")
        if(sub[1] == "txt"):
            fullpath = join(catPath, sub[0]+fileType)
            #print(fullpath)
            fp.write(fullpath + "\n")

fp.close()
