#!/bin/bash

sudo yum install nginx docker docker.x86_64 -y
sudo systemctl restart nginx
sudo systemctl restart docker

sudo usermod -a -G docker ec2-user
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

