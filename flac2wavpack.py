#!/usr/bin/env python2
# foo
"""
"""
from sys import argv
from os import walk, devnull, unlink
from os.path import join, exists, isdir
from subprocess import call
from mutagen import File
from functools import partial

WAVPACK = "/usr/bin/wavpack"
WAVPACK_OPTIONS = ["-b400", "-cc", "-c", "-m"]
WAVPACK_COMMAND = [WAVPACK] + WAVPACK_OPTIONS
FLAC_COMMAND = ["/usr/bin/flac", "-sd"]
mycall = partial(call, stderr=open(devnull,"w"))

def transfer_tags(flacfile, wavpackfile):
    """docstring for transfer_tags"""
    fl = File(flacfile)
    wv = File(wavpackfile)
    wv.update(fl)

    try:
        wv["track"] = wv["tracknumber"]
        del wv["tracknumber"]
        if wv["totaltracks"]:
           wv["track"] = wv["track"][0] + "/" + wv["totaltracks"][0]
           del wv["totaltracks"]
        wv["disc"] = wv["discnumber"]
        del wv["discnumber"]
        if wv["totaldiscs"]:
           wv["disc"] = wv["disc"][0] + "/" + wv["totaldiscs"][0]
           del wv["totaldiscs"]
    except KeyError:
        pass

    wv.save()

def main():
    """docstring for main"""
    if len(argv) != 2:
        exit(__doc__)

    if not exists(argv[1]) or not isdir(argv[1]):
        exit(argv[1] + "does not exist")

    for dir, _, files in walk(argv[1]):
        for f in files:
            if not f[-4:].lower() == "flac":
                continue

            flacfile = join(dir, f)
            wavfile = flacfile.replace(".flac", ".wav")
            wavpackfile = flacfile.replace(".flac", ".wv")

            if exists(wavpackfile):
                print wavpackfile, "exists, skippping", flacfile
                continue
            else:
                print "working on", flacfile

            flacprocess = mycall(FLAC_COMMAND + [ flacfile ])
            if not flacprocess == 0:
                print "error on", flacfile
                continue

            wvprocess = mycall(WAVPACK_COMMAND + [wavfile, "-o", wavpackfile])
            if not wvprocess == 0:
                print "error on", wavpackfile
                continue

            unlink(wavfile)

            transfer_tags(flacfile, wavpackfile)


if __name__ == '__main__':
    main()
