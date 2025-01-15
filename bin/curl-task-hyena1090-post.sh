#!/bin/bash
#
# Title: curl-task-hyena1090.sh
# Description: create hyena 1090 task 
# Development Environment: Ubuntu 18.04.3 LTS (Bionic Beaver)
# Author: G.S. Cole (guycole at gmail dot com)
#
#PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
HOST_URL="localhost:8000"
#
TASK_ID=$(uuidgen)
PAYLOAD='{"id": "'$TASK_ID'", "active_flag": true, "name": "hyena-1090"}'
#echo $PAYLOAD
#
curl -v -H "Content-Type: application/json" -d "$PAYLOAD" http://$HOST_URL/task/
#