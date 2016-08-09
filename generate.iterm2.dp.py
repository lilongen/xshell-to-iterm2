#!/usr/bin/python
#

import sys
import re
import os
from jinja2 import Template, Environment, FileSystemLoader


P = re.compile(r'^\./(?P<dirs>.*)/(?P<name>.+)\.xsh')
Xsh_Info= []

def convertXshHierarchy2Iterm2Tags(hierarchyDirs):
	arr = hierarchyDirs.split('/')
	tags = []
	tagName = ''
	for i in range(len(arr)):
		if i > 0:
			tagName += ' | '
		tagName += arr[i]
		tags.append(tagName)
	return '[' + ', '.join('"' + item + '"' for item in tags) + ']'

def getConnInfo(strConn):
	arr = strConn.split(',')
	return {
		'ip': arr[0],
		'port': arr[1],
		'username': arr[2],
		'password': arr[3]
	}

def extractSessionInfo(line):
	global P
	arr = line.split('\t');
	m = P.search(arr[0])
	name = m.group('name')	
	conn = getConnInfo(arr[1])
	tags = convertXshHierarchy2Iterm2Tags(m.group('dirs'))

	return {
		'ip': conn['ip'],
		'port': conn['port'],
		'username': conn['username'],
		'password': conn['password'],
		'name': name,
		'tag': tags
	}


def renderIterm2DynamicProfileTpl():
	tplLocation = os.path.dirname(os.path.abspath(__file__))
	env = Environment(loader=FileSystemLoader(tplLocation))
	template = env.get_template('iterm2.dynamic.profile.tpl')
	
	fh = open('iterm2.dp', 'w')
	fh.write(template.render(profiles=Xsh_Info))
	fh.close()
		

def main():
	global Xsh_Info
	fXSHs = open(sys.argv[1])
	for line in fXSHs:
		line = line[:-1]
		print "converting {} ... ".format(line)
		info = extractSessionInfo(line)
		Xsh_Info.append(info)
	fXSHs.close()

	renderIterm2DynamicProfileTpl()

main()

