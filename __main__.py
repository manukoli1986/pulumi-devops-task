import pulumi
import pulumi_aws as aws

# Create a VPC (same as before)
vpc = aws.ec2.Vpc("my-vpc", cidr_block="10.0.0.0/16")

# Create an Internet Gateway and associate it with the VPC
public_subnet_gateway = aws.ec2.InternetGateway("public-subnet-gateway",
    vpc_id=vpc.id,
)

# Create a public subnet with an Internet Gateway
public_subnet = aws.ec2.Subnet("public-subnet",
    vpc_id=vpc.id,
    cidr_block="10.0.1.0/24",  # Adjust the CIDR block as needed
    availability_zone="us-east-1a",  # Replace with your desired availability zone
    map_public_ip_on_launch=True,
)

# Create a route table for the public subnet
route_table = aws.ec2.RouteTable("public-subnet-route-table",
    vpc_id=vpc.id,
)

# Create a route in the route table to the Internet Gateway
route = aws.ec2.Route("public-subnet-route",
    route_table_id=route_table.id,
    destination_cidr_block="0.0.0.0/0",
    gateway_id=public_subnet_gateway.id,
)

# Associate the route table with the public subnet
route_table_association = aws.ec2.RouteTableAssociation("public-subnet-association",
    subnet_id=public_subnet.id,
    route_table_id=route_table.id,
)

# Create a Security Group for the EC2 instance (same as before)
ec2_sg = aws.ec2.SecurityGroup("ec2-sg",
    vpc_id=vpc.id,
    ingress=[
        aws.ec2.SecurityGroupIngressArgs(
            protocol="-1",  # Allow all protocols
            from_port=0,    # Allow traffic from all ports
            to_port=0,      # Allow traffic to all ports
            cidr_blocks=["0.0.0.0/0"],  # Allow traffic from anywhere
        ),
    ],
    egress=[
        aws.ec2.SecurityGroupEgressArgs(
            protocol="-1",  # Allow all protocols
            from_port=0,    # Allow traffic from all ports
            to_port=0,      # Allow traffic to all ports
            cidr_blocks=["0.0.0.0/0"],  # Allow traffic to anywhere
        ),
    ],
)

ec2_instance = aws.ec2.Instance("web-ui-instance",
    ami="ami-051f7e7f6c2f40dc1",  # Replace with your preferred AMI ID
    instance_type="t2.medium",  # Adjust the instance type as needed
    subnet_id=public_subnet.id,
    vpc_security_group_ids=[ec2_sg.id],
    user_data=f"""#!/bin/bash
        sudo mkdir /app && sudo yum install git -y && sudo git clone https://github.com/manukoli1986/pulumi-devops-task.git /app && sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose && sudo sh +x /app/my-amazing-script.sh  && cd /app && sudo docker-compose up --build
    """,
    user_data_replace_on_change=True,
)

# Tag resources for auditing purposes (as needed)

# Output the public IP of the EC2 instance (same as before)
pulumi.export("ec2_public_ip", ec2_instance.public_ip)
