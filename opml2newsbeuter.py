#!/usr/bin/python
#this script converts a simple .opml-file to
#an urls-file to use with newsbeuter
#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# Wieland Hoffmann (the_mineo at web dot de) wrote this file. As long as you 
# retain this notice you can do whatever you want with this stuff. If we meet
# some day, and you think this stuff is worth it, you can buy me a beer in
# return 
# ----------------------------------------------------------------------------

  
from xml.dom.minidom import parse
import sys

try:
	input = sys.argv[0]
	output = sys.argv[1]
except:
	print "usage: opml2newsbeuter.py input-file output-file"
	sys.exit()

try:
	opml = parse(input)
except:
	print "couldn't open the input file"
	sys.exit()

outlines = opml.getElementsByTagName('outline')
dict ={}
tag = "newtag"
for line in outlines:
	try:
		url = line.attributes["xmlUrl"].value
		if dict.has_key(tag):
			dict[tag].append(url)
		else:
			dict[tag] = []
			dict[tag].append(url)
		print "NEW URL", line.attributes["xmlUrl"].value, "WITH TAG", tag
	except:
		try:
			tag = line.attributes["text"].value
			print "CHANGED TAG TO", tag
		except:
			print "ERROR line contains neither tag nor url"

outfile = open(output,'w')
for key in dict.keys():
	for new_url in dict[key]:
		line2write = new_url + " \"" + key +"\"\n"
		outfile.write(line2write)

outfile.close()
