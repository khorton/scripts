#! /bin/sh

# setup ssh tunnel between Mac Mini and Linode server

/opt/local/bin/autossh -M 5234 -N -f -T -R 22222:localhost:22 45.33.33.133