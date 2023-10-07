#!/usr/bin/env python3

import glob
import hashlib
import mmap
import sys
import os

MAX_STRIDE = 100*1024*1024  # 100MB

def usage():
    print(str(sys.argv[0]) + ' <path> <outfile>')

def hashfiles(filelist):
    hashdict = {}
    for f in filelist:
        try:
            file_size = os.path.getsize(f)
            if file_size is 0: continue
            with open(f, 'rb') as fobj:
                print('Adding ' + str(f))
                h = hashlib.sha1()
                fptr = 0
                while fptr < file_size:
                    stride = min(file_size - fptr, MAX_STRIDE)
                    with mmap.mmap(fobj.fileno(), 
                                   stride, 
                                   access=mmap.ACCESS_READ,
                                   offset=fptr) as mm:
                        mm.madvise(mmap.MADV_SEQUENTIAL)
                        h.update(mm.read())
                    fptr += stride
                h = h.hexdigest()
                try:
                    hashdict[h].append(str(f))
                except KeyError:
                    hashdict[h] = [str(f)]
        except IsADirectoryError:
            pass
    return hashdict

def writecsv(hashlist, filename):
    with open(filename, 'w') as fobj:
        for h in hashlist.keys():
            fobj.write(h + ''.join([',' + f for f in hashlist[h]]))
            fobj.write('\n')
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

