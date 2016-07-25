#!/usr/bin/python
#

import re

P = re.compile(r'[^/]*/(?P<dirs>.*)/(?P<name>.+)\.xsh')

def extractSessionInfo(line):
	global P
	arr1 = line.split(';');
	m = P.search(arr[0])

	return {
		'ip': arr1[1], 
		'name': m.group('name'),
		'tag': m.group('dirs').split('/')
	}


def main():
	with open("_xshell.sessions.info") as fXSHs
		for line in fXSHs:
			info = extractSessionInfo(line)
			print info

