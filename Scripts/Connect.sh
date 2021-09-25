#!/bin/bash
while true
do
socat -u TCP:0.0.0.0:30005 TCP:centurionx.net:30004
echo "Looks like we lost connection"
sleep 5
done
