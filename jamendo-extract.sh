#!/bin/sh
# no bloating text
# ------------------------------
# extract jamendo zip-files into
# a new directory named after
# the zip-file as they have no
# internale folder structure
# ------------------------------
clear
newdir=`echo $1 | sed 's/.zip//'`
mkdir "$newdir"
mv "$1" "$newdir"
cd "$newdir"
7z x "$1"
rm "$1"
