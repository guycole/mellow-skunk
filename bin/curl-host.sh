#!/bin/bash
#
# Title: curl-host.sh
# Description: read host information
# Development Environment: Ubuntu 18.04.3 LTS (Bionic Beaver)
# Author: G.S. Cole (guycole at gmail dot com)
#
#PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
HOST_URL="localhost:8000"
#
curl -v http://$HOST_URL/host/
#