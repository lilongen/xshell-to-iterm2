#!/bin/bash
#

XshellSessionLocation=$1
cd $XshellSessionLocation
find  .  -name "*.xsh" -exec echo -n "{};" \; -exec grep -o -P "(?<=^Host=)([\w\-\.]+)" "{}" \; > _xshell.sessions.info
