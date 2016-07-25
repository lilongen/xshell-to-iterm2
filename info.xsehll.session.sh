#!/bin/bash
#

find $XshellSessionLocation -name *.xsh -exec echo -n "{};" \; -exec grep -o -P "(?<=^Host=)(.+)" "{}" \; > _xshell.sessions.info
