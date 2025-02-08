#!/bin/bash
#
# Title: curl-poodle-test-post.sh
# Description: poodle observations
# Development Environment: Ubuntu 18.04.3 LTS (Bionic Beaver)
# Author: G.S. Cole (guycole at gmail dot com)
#
#PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
HOST_URL="localhost:8000"
#
PAYLOAD='{"humidity_pct": 12.34, "temperature_c": 23.45, "pressure_mb": 34.56, "orientation_pitch_rads": 45.67, "orientation_roll_rads": 56.78, "orientation_yaw_rads": 67.89, "time_stamp_z":"2025-01-12T19:50:25Z"}'
#echo $PAYLOAD
#
curl -v -H "Content-Type: application/json" -d "$PAYLOAD" http://$HOST_URL/poodle/
#
