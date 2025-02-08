#!/bin/bash
#
# Title: curl-heeler-test-post.sh
# Description: heeler observations
# Development Environment: Ubuntu 18.04.3 LTS (Bionic Beaver)
# Author: G.S. Cole (guycole at gmail dot com)
#
#PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
HOST_URL="localhost:8000"
#
PAYLOAD='[{"bssid":"address1","ssid":"essid1","frequency_mhz":1,"time_stamp_z":"2025-01-12T12:34:56Z"},{"bssid":"address2","ssid":"essid3","frequency_mhz":2,"time_stamp_z":"2025-01-12T19:50:25Z"}]'
#echo $PAYLOAD
#
curl -v -H "Content-Type: application/json" -d "$PAYLOAD" http://$HOST_URL/heeler/
#
