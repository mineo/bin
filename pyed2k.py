#!/usr/bin/python
""" Calculates the ed2k hash of one or more files """
import hashlib

def md4(chunk):
    """ if hashlib.update of an object is called several times with hashes
    a, b, c, ... the returned hash is the hash of (a+b+c+...) so this needs a
    new hash object every time """
    m = hashlib.new("md4")
    m.update(chunk)
    return m

def hash(file):
    hash = hashlib.new("md4")
    while True:
        chunk = file.read(9728000)
        if chunk:
            hash.update(md4(chunk).digest())
        else:
            break
    return hash.hexdigest()


if __name__ == "__main__":
    import sys
    for filename in sys.argv[1:]:
        with open(filename,"rb") as file:
            print file, " ", hash(file)
