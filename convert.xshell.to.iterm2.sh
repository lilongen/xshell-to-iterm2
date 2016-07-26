#!/bin/bash
#

XshellSessionLocation=$1
./info.xshell.session.sh "$XshellSessionLocation"
python ./generate.iterm2.dp.py "/tmp/_xshell.sessions.info"