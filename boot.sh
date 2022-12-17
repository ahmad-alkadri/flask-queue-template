#!/bin/sh
if [ $( docker ps -a | grep redis-stack-server | wc -l ) -gt 0 ]; then
  echo "redis-stack-server exists and running"
else
  echo "redis-stack-server does not exist, running it now"
  docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
fi

if [ ! -f .locenv/bin/activate ]
then
    echo "Local environment isn't found. Initiating..."
    python3 -m pip install virtualenv
    python3 -m virtualenv .locenv
    source .locenv/bin/activate
    python3 -m pip install -r requirements.txt
else
    echo "Local environment found. Activating it..."
    source .locenv/bin/activate
    python3 -m pip install -r requirements.txt
fi

./app.py
