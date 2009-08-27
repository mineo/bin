#!/bin/sh
# no bloating text
# ------------------------------
# extract jamendo zip-files into
# a new directory named after
# the zip-file as they have no
# internale folder structure
# ------------------------------

musicdir=/media/crypt/Musik
for i in "$*"; do
	newdir=`echo $i | sed 's/.zip//'`
	mkdir "$newdir"
	mv "$i" "$newdir"
	cd "$newdir"
	7z x "$i"
	rm "$i"
	cd ..
	mv "$newdir" $musicdir
done
