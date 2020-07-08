# Baibumblebee
Project Baibumblebee
environment:
1. install git
2. install conda
3. install supervisor
4. install lsof

baibumblebee.sh:
#!/bin/bash
cd /opt/Baibumblebee
source activate Baibumblebee
exec python route.py

supervisord.conf:
[program:Baibumblebee]
command= /opt/baibumblebee.sh
autorestart=true
user=root
startretries=3

rewrite:
1. cd /opt
2. ./rewrite.sh

ps aux|grep 8000

run: 
supervisorctl status Baibumblebee
supervisorctl start Baibumblebee
supervisorctl stop Baibumblebee
