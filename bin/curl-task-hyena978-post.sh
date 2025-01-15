#!/bin/bash
#
# Title: curl-task-hyena978.sh
# Description: create hyena 978 task 
# Development Environment: Ubuntu 18.04.3 LTS (Bionic Beaver)
# Author: G.S. Cole (guycole at gmail dot com)
#
#PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
HOST_URL="localhost:8000"
#
TASK_ID=$(uuidgen)
PAYLOAD='{"id": "'$TASK_ID'", "active_flag": true, "name": "hyena-978"}'
#echo $PAYLOAD
#
curl -v -H "Content-Type: application/json" -d "$PAYLOAD" http://$HOST_URL/task/
#