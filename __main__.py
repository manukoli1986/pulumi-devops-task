import pulumi
import pulumi_aws as aws

# Create a VPC (same as before)
vpc = aws.ec2.Vpc("my-vpc", cidr_block="10.0.0.0/16")

# Create a Security Group for the EC2 instance
ec2_sg = aws.ec2.SecurityGroup("ec2-sg",
    vpc_id=vpc.id,
    ingress=[
        aws.ec2.SecurityGroupIngressArgs(
            protocol="tcp",
            from_port=80,
            to_port=80,
            cidr_blocks=["0.0.0.0/0"],  # Allow traffic from anywhere (for demonstration purposes)
        ),
    ],
)

# Create an EC2 instance with Docker and Docker Compose
ec2_instance = aws.ec2.Instance("web-ui-instance",
    ami="ami-051f7e7f6c2f40dc1",  # Replace with your preferred AMI ID
    instance_type="t2.medium",  # Adjust the instance type as needed
    vpc_security_group_ids=[ec2_sg.id],
    user_data=f"""#!/bin/bash
        # Install Docker and Docker Compose
        sudo yum update -y
        sudo amazon-linux-extras install -y docker
        sudo service docker start
        sudo usermod -a -G docker ec2-user
        sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        sudo chmod +x /usr/local/bin/docker-compose

        # Clone the GitHub repository
        git clone https://github.com/test/test.git /app

        # Change directory to where the docker-compose.yml file is located
        cd /app

        # Run Docker Compose to start the application
        docker-compose up -d
    """,
)

# Tag resources for auditing purposes (as needed)

# Output the public IP of the EC2 instance
pulumi.export("ec2_public_ip", ec2_instance.public_ip)
