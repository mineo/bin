#!/usr/bin/python
import sys
from calendar import timegm

debug = True

class Song( object ):
	def __init__(self,raw):
		self.artist = raw[1]
		self.title = raw[2]
		self.album = raw[3]
		self.playtime = raw[4]
		self.length = raw[5]
		if debug:
			print "Artist ",self.artist
			print "Title ",self.title
			print "Album ",self.album
			print "Length ",self.length
			print "Playtime ",self.playtime
			print "\n"

class Songs( object ):
	def __init__(self):
		self.songs = []
	
	def addSong(self,song):
		if len(self.songs)<50:
			song = Song(song)
			self.songs.append(song)
		else:
			pass #submit

def printSongs(self):
		for self.song in self.songs:
			print self.song

class MusicLog(object):
	def __init__(self):
		pass
	
	def readLog(self,file="music.log"):
		try:
			self.file = open(file,"r")
		except IOError:
			print "Error opening ",file
			sys.exit()
		for self.line in self.file:
			self.line = self.line.split(',')
			self.line.append(mkUnixTime(self.line[1]))
			self.line.append(getLengthInSeconds(self.line[6]))
			self.line[1] = self.line[1].split(' ')
			del self.line[0]
			del self.line[4:7]
			songs.addSong(self.line)
		self.file.close()

def mkUnixTime(time):
	time = time.replace(' ',':').split(':')
	time = [int(x) for x in time]
	time = timegm(time)
	return time

def getLengthInSeconds(length):
	length = length.split(':')
	length = [int(x) for x in length]
	length = length[0]*3600+length[1]*60+length[2]
	return length
	

songs = Songs()
log = MusicLog()
log.readLog()
