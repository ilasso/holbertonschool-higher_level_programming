#!/bin/bash
# sends a request URL, and returns the size of the body
curl -sI "$1"|grep "Content-Length:"|cut -d" " -f 2
