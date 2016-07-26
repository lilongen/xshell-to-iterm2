#!/bin/bash
#

XshellSessionLocation=$1
cd $XshellSessionLocation
os=$(uname -a)

if [[ $os == "Linux"* ]]; then
	find  .  -name "*.xsh" -exec echo -n "{};" \; -exec grep -o -P "(?<=^Host=)([\w\-\.]+)" "{}" \; > /tmp/_xshell.sessions.info
else 
	find  .  -name "*.xsh" -exec echo -n "{};" \; -exec perl -nle 'print $1 if m{(?<=^Host=)([\w\.\-]+)}' "{}" \; > /tmp/_xshell.sessions.info
fi
