#!/usr/bin/python
##########################################################
# join all part files in a dir created by split.py.  
# This is roughly like a 'cat fromdir/* > tofile' command
# on unix, but is a bit more portable and configurable,
# and exports the join operation as a reusable function.
# Relies on sort order of file names: must be same length.
# Could extend split/join to popup Tkinter file selectors.
##########################################################

import os, sys
import glob
readsize = 1024

def join(fromdir, tofile):
    output = open(tofile, 'wb')
    parts=glob.glob(fromdir+'\part0???')
    print parts
    for filename in parts:
        fileobj  = open(filename, 'rb')
        while 1:
            filebytes = fileobj.read(readsize)
            if not filebytes: break
            output.write(filebytes)
        fileobj.close(  )
    output.close(  )
join
if __name__ == '__main__':

    fromdir = "."
    tofile  = ".\\Output.zip"

    absfrom, absto = map(os.path.abspath, [fromdir, tofile])
    print 'Joining', absfrom, 'to make', absto

    try:
        join(fromdir, tofile)
    except:
        print 'Error joining files:'
        print sys.exc_type, sys.exc_value
    else:
       print 'Join complete: see', absto