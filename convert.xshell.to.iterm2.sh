#!/bin/bash
#

XshellSessionLocation=$1
echo scanning xshell session profiles ...
./info.xshell.session.sh "$XshellSessionLocation"
echo done

echo converting xshell profiles to iterm2 dynamic profiles ...
python ./generate.iterm2.dp.py "/tmp/_xshell.sessions.info"
echo done