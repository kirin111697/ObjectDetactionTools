#-*- encoding:utf-8 -*-
from os import walk, stat
from os.path import join
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="define the path of the files")
args = parser.parse_args()
labelCnt = [] # -1: empty, -2:labels
totalCnt = 0

if args.path:
    path = args.path
else:
    path = "Z:\Zen\Label\mark2"

classFile = open(join(path, "classes.txt"), "r")
for c in classFile:
    c = c.replace("\n", "")
    labelCnt.append([c, 0])
labelCnt.append(["labels", 0])
labelCnt.append(["empty", 0])

fEmpty = open(join(path, "emptyList.txt"), "w")
fLabel = open(join(path, "labelList.txt"), "w")

for root, dirs, files in walk(path):
    for f in files:
        if f == "classes.txt":
            continue
        totalCnt += 1
        filePath = join(root, f)
        if stat(filePath).st_size == 0:
            labelCnt[-1][1] += 1
            fEmpty.write(f+"\n")
        else:
            labelCnt[-2][1] += 1
            fLabel.write(f+"\n")
            f = open(join(root, f), "r", encoding="utf-8")
            for l in f:
                index = int(l.split(" ")[0])
                labelCnt[index][1] += 1

fEmpty.write("total count: " + str(labelCnt[-1][1]))
#print(labelCnt)
for item in labelCnt:
    fLabel.write(item[0] + ": " + str(item[1]) + "\n")
    print(item[0] + ": " + str(item[1]))
fLabel.write("total count: " + str(labelCnt[-2][1]))
print("Total Count is " + str(totalCnt))
