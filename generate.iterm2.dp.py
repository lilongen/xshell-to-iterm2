#!/usr/bin/python
#

import re
import os
from jinja2 import Template, Environment, FileSystemLoader


P = re.compile(r'^\./(?P<dirs>.*)/(?P<name>.+)\.xsh')
Xsh_Info= []

def extractSessionInfo(line):
	global P
	arr = line.split(';');
	m = P.search(arr[0])

	return {
		'ip': arr[1][:-1], 
		'name': m.group('name'),
		'tag': m.group('dirs').split('/')
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
	fXSHs = open("_xshell.sessions.info")
	for line in fXSHs:
		info = extractSessionInfo(line)
		Xsh_Info.append(info)
	fXSHs.close()

	renderIterm2DynamicProfileTpl()

main()

