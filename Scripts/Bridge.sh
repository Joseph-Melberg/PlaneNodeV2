#!/bin/bash
while true
do
ssh -o ServerAliveInterval=60 -R 7101:localhost:22 jump@jump.centurionx.net "./KeepAlive.sh $HOSTNAME"
sleep 10
done
