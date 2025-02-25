#!/bin/bash
#
# Title: curl-hyena-test-post.sh
# Description: hyena-observations
# Development Environment: Ubuntu 18.04.3 LTS (Bionic Beaver)
# Author: G.S. Cole (guycole at gmail dot com)
#
#PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
HOST_URL="localhost:8000"
#
PAYLOAD='[ {"flight": "flight1", "hex": "hex1", "time_stamp": "2025-01-12T19:50:25.584981Z"}, {"flight": "flight2", "hex": "hex2", "time_stamp": "2025-01-12T19:50:25.584981Z"}]'
#echo $PAYLOAD
#
curl -v -H "Content-Type: application/json" -d "$PAYLOAD" http://$HOST_URL/hyena/
#

