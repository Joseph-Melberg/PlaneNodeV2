#!/bin/bash
cd $(dirname $BASH_SOURCE)
echo "Starting heartbeat"
./Scripts/Heartbeat.sh >> /dev/null & 
echo "Starting plane"
./Scripts/Plane.sh  >> /dev/null &
echo "Starting plane connection"
./Scripts/Connect.sh >> /dev/null &  
echo "Starting Temp logging"
./Scripts/Temp.sh >> /dev/null &
sleep infinity
