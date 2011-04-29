#!/usr/bin/env python2
"""Deletes the day and month from the 'date' tag in music files"""
import sys
try:
    import mutagen
except ImportError:
    sys.exit("You need mutagen to use this")

from os import walk
from os.path import join

if len(sys.argv) == 2:
    basedir = sys.argv[1]
else:
    sys.exit("Usage: %s directory" % sys.argv[0])

for root, dirs, files in walk(basedir):
    for name in files:
        print "Working on %s:" % join(root, name),
        mufile = mutagen.File(join(root, name), easy=True)
        if mufile is not None:
            if "date" in mufile.keys():
                mufile["date"] = [mufile["date"][0][:4]]
                mufile.save()
                print mufile["date"][0]
            else:
                print "No date to fix :-( "
