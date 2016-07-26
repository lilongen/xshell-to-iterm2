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

def extractSessionInfo(line):
	global P
	arr = line.split(';');
	m = P.search(arr[0])
	tags = convertXshHierarchy2Iterm2Tags(m.group('dirs'))
	return {
		'ip': arr[1][:-1], 
		'name': m.group('name'),
		'tag': tags
	}


def renderIterm2DynamicProfileTpl():
	tplLocation = os.path.dirname(os.path.abspath(__file__))
	env = Environment(loader=FileSystemLoader(tplLocation))
	template = env.get_template('iterm2.dynamic.profile.tpl')
	print template.render(profiles=Xsh_Info)
	
	fh = open('iterm2.dp', 'w')
	global Xsh_Info
	fh.write(template.render(profiles=Xsh_Info))
	fh.close()
		

def main():
	global Xsh_Info
	fXSHs = open(sys.argv[1])
	for line in fXSHs:
		info = extractSessionInfo(line)
		Xsh_Info.append(info)
	fXSHs.close()

	renderIterm2DynamicProfileTpl()

main()

