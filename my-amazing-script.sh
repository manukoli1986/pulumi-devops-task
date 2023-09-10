#!/bin/bash
sudo mkdir /app
sudo yum update -y
sudo yum install nginx docker docker.x86_64 -y
sudo systemctl restart nginx

sudo yum update -y
sudo yum install nginx -y
sudo yum -y docker git
sudo systemctl docker start docker.x86_64
sudo usermod -a -G docker ec2-user
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo mkdir /app
sudo chmod 777 -R /app
# Clone the GitHub repository
git clone https://github.com/manukoli1986/pulumi-devops-task.git /app
# Change the directory to where the docker-compose.yml file is located
cd /app
# Run Docker Compose to start the application
sudo docker-compose up -d —build
