#!/bin/bash

ip=192.168.10.20
[ "$1" != "" ] && ip=$1

ssh root@$ip mkdir /www/cgi-bin/
scp ../www_cgi-bin/relay.cgi root@$ip:/www/cgi-bin/

