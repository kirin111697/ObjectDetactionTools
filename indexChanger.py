from os import walk, stat
from os.path import join
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="define the path of the files")
parser.add_argument("index", type=int, help="labels to be alter")
parser.add_argument("intervel", type=int, help="intervel to the target class, ex: set the intervel to 2 to change class 1 to 3")
parser.add_argument("-r", "--reverse", help="set this flag to reverse the indexs' changing from increase to decrease", action="store_true")
parser.add_argument("-re", "--recur", help="set this flag to also alter the following classes in the same rule", action="store_true")
args = parser.parse_args()

if args.path:
    path = args.path
else:
    path = "Z:\Zen\Label\mark1\\1"

log = open(join(path, "log.txt"), "w")

for root, dirs, files in walk(path):
    for f in files:
        targetPath = join(root, f)
        if f == "classes.txt":
            continue
        if stat(targetPath).st_size == 0:
            continue
        print(f +  ":")
        log.write(f +  ":\n")
        target = open(targetPath, "r")
        lines = target.readlines()
        target.close()
        target = open(targetPath, "w")
        for l in lines:
            parts = l.split(" ")
            newLine = ""
            if args.recur:
                if int(parts[0]) >= args.index:
                    if args.reverse:
                        newLine = str(int(parts[0]) - args.intervel) + l[len(parts[0]):]
                    else:
                        newLine = str(int(parts[0]) + args.intervel) + l[len(parts[0]):]
            else:
                if int(parts[0]) == args.index:
                    if args.reverse:
                        newLine = str(int(parts[0]) - args.intervel) + l[len(parts[0]):]
                    else:
                        newLine = str(int(parts[0]) + args.intervel) + l[len(parts[0]):]
            if newLine != "":
                target.write(newLine)
                log.write(l[:-1] + " --> " + newLine)
            else:
                target.write(l)
                log.write(l)

        target.close()
        log.write("\n")
        
log.close()
