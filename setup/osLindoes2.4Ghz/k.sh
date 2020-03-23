#!/bin/bash



echo -e "\n\nsenha: p9z34c\n\n\n"

rm .ssh/known_hosts 
echo -e 'yes\n' | ssh-copy-id root@192.168.10.253
echo -e 't\nt\n' | ssh root@192.168.10.253 passwd

scp ./wireless   root@192.168.10.253:/etc/config/
scp ./network    root@192.168.10.253:/etc/config/
ssh root@192.168.10.253 reboot
