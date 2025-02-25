#!/bin/bash
#
# Title: curl-host-rpi3d-post.sh
# Description: create host rpi3d 
# Development Environment: Ubuntu 18.04.3 LTS (Bionic Beaver)
# Author: G.S. Cole (guycole at gmail dot com)
#
#PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
HOST_URL="localhost:8000"
#
PAYLOAD='{"active_flag":true,"location":"vallejo","host":"rpi3d","latitude":12.34,"longitude":123.45,"type":"rpi3"}'
#echo $PAYLOAD
#
curl -v -H "Content-Type: application/json" -d "$PAYLOAD" http://$HOST_URL/host/
#