#!/bin/sh
# make git use FileMerge as the diff tool
# from http://www.jotlab.com/2009/how-to-use-filemerge-with-git-as-a-diff-tool-on-osx
/usr/bin/opendiff "$2" "$5" -merge "$1"