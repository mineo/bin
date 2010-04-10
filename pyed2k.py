#!/usr/bin/python
""" Calculates the ed2k hash of one or more files """
import hashlib
import sys

def md4(chunk):
	" if hashlib.update of an object is called several times with hashes
	a, b, c, ... the returned hash is the hash of (a+b+c+...) so this needs a
	new hash object every time "
	m = hashlib.new("md4")
	m.update(chunk)
	return m

def hash(filename):
	hashes = []
	with open(filename,"rb") as file:
		while True:
			chunk = file.read(9728000)
			if chunk:
				hashes.append(md4(chunk).digest())
			else:
				break
	hash = reduce(lambda x,y: x+y, hashes, "")
	return md4(hash).hexdigest()


if __name__ == "__main__":
	for file in sys.argv[1:]:
		print file, " ", hash(file)
