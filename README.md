# xshell2iterm2

convert Xshell session profiles to iTerm2 Dynamic Profiles tools


## requirements
```
1. bash
2. python, python jinja2
```

## usage
```
1. cd %Xshell2item2_Location%
2. ./convert.xshell.to.iterms.sh %Xshell_Session_Profiles_Location%
```
## example

```
if xshell session profiles locate at "/opt/ciom/port/xshell/Sessions" 
# tree /opt/ciom/port/xshell/Sessions
/opt/ciom/port/xshell/Sessions
├── iis
│   ├── 172.17.128.180.xsh
│   ├── 172.17.128.181.xsh
├── mysql
│   ├── 172.17.128.211.xsh
│   ├── 172.17.128.213.xsh
├── web server
│   ├── 172.17.128.191.xsh
│   ├── 172.17.128.193.xsh
│   ├── tomcat
│   │   ├── 172.17.128.150.xsh
│   │   ├── 172.17.128.151.xsh
...

then %Xshell_Session_Profiles_Location% is "/opt/ciom/port/xshell/Sessions"

# ./convert.xshell.to.iterms.sh /opt/ciom/port/xshell/Sessions
generated iterm2.dp under %Xshell2item2_Location% is the converted iterm2 dynamic profile config file.
```
