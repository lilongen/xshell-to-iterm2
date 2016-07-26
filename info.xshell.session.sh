#!/bin/bash
#

XshellSessionLocation=$1
cd $XshellSessionLocation
find  .  -name "*.xsh" \
	-exec printf "%s\t" "{}" \; \
	-exec perl -nle 'printf("%s,", $1) if m{(?<=^Host=)([\w\.\-]+)}' "{}" \; \
	-exec perl -nle 'printf("%s,", $1) if m{(?<=^Port=)([\d]+)}' "{}" \; \
	-exec perl -nle 'printf("%s,", $1) if m{(?<=^UserName=)([\w]+)}' "{}" \; \
	-exec perl -nle 'printf("%s\n", $1) if m{(?<=^Password=)([^\s\r\n]*)}' "{}" \; \
	> /tmp/_xshell.sessions.info
