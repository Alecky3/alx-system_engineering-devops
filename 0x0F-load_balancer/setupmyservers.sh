#!/usr/bin/bash
# Install nginx to my servers and makes necessary configurations.

if [ $# -lt 2 ]
then
	echo "Usage: ./$0 PATH_TO_FILE SSH_KEY"
else
	scp -o StrictHostKeyChecking=no -i "$2" "$1" "ubuntu@18.209.223.27":~
	scp -o StrictHostKeyChecking=no -i "$2" "$1" "ubuntu@100.25.118.39":~
fi
