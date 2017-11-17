#!/usr/bin/env python3

import glob
import hashlib
import sys

def usage():
    print(str(sys.argv[0]) + ' <path> <outfile>')

def hashfiles(filelist):
    hashdict = {}
    for f in filelist:
        try:
            with open(f, 'rb') as fobj:
                print('Adding ' + str(f))
                h = hashlib.sha1(fobj.read()).hexdigest()
                try:
                    hashdict[h].append(str(f))
                except KeyError:
                    hashdict[h] = [str(f)]
        except IsADirectoryError:
            pass
    return hashdict

def writecsv(hashlist, filename):
    with open(filename, 'w') as fptr:
        for h in hashlist.keys():
            fptr.write(h + ''.join([',' + f for f in hashlist[h]]))
            fptr.write('\n')
    return


#print(str(sys.argv))

try:
    PATH = str(sys.argv[1])
    outfile = str(sys.argv[2])
except Exception as e:
    print(str(e))
    usage()
    sys.exit(1)

filelist = glob.glob(PATH + '/**/*', recursive=True)

hashlist = {}
hashlist = hashfiles(filelist)


print(str(len(hashlist)) + ' unique hashes')
writecsv(hashlist, outfile)
print('File ' + str(outfile) + ' written.')

