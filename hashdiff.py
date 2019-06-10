#!/usr/bin/env python3

import glob
import hashlib
import sys

def usage():
    print(str(sys.argv[0]) + ' <hashlistfile_left> <hashlistfile_right>')


#####################
# csv format:
# <hash string, 40 chars>,<file1>,...
# at least 1 file present

def load_dict(csvfile):
    hashdict = {}
    badlines = 0
    goodlines = 0
    with open(csvfile, 'r') as fptr:
        for l in fptr.readlines():
            s = l.split(',')
            if ((len(s) < 2) or (len(s[0]) is not 40)):
                print('Bad line <' + l + '>')
                badlines += 1
                continue
            hashdict[s[0]] = ','.join(s[1:])
            goodlines += 1
    return (hashdict, goodlines)


try:
    listfile_left = str(sys.argv[1])
    listfile_right = str(sys.argv[2])
except Exception as e:
    print(str(e))
    usage()
    sys.exit(1)

(hashdict_left, goodlines) = load_dict(listfile_left)
print('Loaded ' + str(goodlines) + ' hashes from ' + listfile_left + '.')
(hashdict_right, goodlines) = load_dict(listfile_right)
print('Loaded ' + str(goodlines) + ' hashes from ' + listfile_right + '.')

hashes_left = hashdict_left.keys()
hashes_right = hashdict_right.keys()

hashes_in_left_but_not_right = []
for h in hashes_left:
    if h not in hashes_right:
        hashes_in_left_but_not_right.append(h)

print(str(len(hashes_in_left_but_not_right)) + ' hashes are in left but not right:')
for h in hashes_in_left_but_not_right:
    print(h + ' ' + hashdict_left[h].strip())


        
