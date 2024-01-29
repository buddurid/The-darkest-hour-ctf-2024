#!/bin/sh

# Create a file with a random name with the prefix /flag
echo $FLAG > /flag_$(cat /dev/urandom | tr -dc 'a-f0-9' | fold -w 20 | head -n 1)
unset FLAG
echo "Challenge star"
su ctf -c "./ynetd -p $PORT ./main"
