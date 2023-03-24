#!/bin/bash

cd /home/ubuntu/kokorofoods2.0

sudo docker-compose build
sudo docker-compose up -d --force-recreate
sudo docker image prune -f