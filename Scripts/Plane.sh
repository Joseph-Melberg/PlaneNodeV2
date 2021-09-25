#!/bin/bash
while true
do
dump1090-mutability --net --quiet --interactive --net-bind-address 0.0.0.0
sleep 5
done
