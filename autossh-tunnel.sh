#! /bin/sh

# setup ssh tunnel between Mac Mini and Linode server

/sw/bin/autossh -M 5234 -N -f -T -R 22222:localhost:22 45.56.64.40
