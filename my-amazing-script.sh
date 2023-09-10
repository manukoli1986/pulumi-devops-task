#!/bin/bash
sudo mkdir /app
sudo yum update -y
sudo yum install nginx docker docker.x86_64 -y
sudo systemctl restart nginx
