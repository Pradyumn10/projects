#!/bin/sh

TIMEOUT="5s"

while : ; do
	python3 bot_discord.py
	echo "Restarting in $TIMEOUT"
	sleep $TIMEOUT
done
