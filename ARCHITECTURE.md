# AWS CloudFormation EC2 Deployment Project

## Overview

This project automates the deployment of an EC2 instance within a custom VPC using AWS CloudFormation. The architecture includes both public and private subnets, along with associated route tables and a NAT Gateway. The EC2 instance is secured to allow SSH access only from a specified public IP address.

## Architecture Components

### 1. VPC
- A new Virtual Private Cloud (VPC) is created with a CIDR block of `10.0.0.0/16`.

### 2. Subnets
- **Public Subnet**: 
  - CIDR Block: `10.0.1.0/24`
  - Configured to assign public IPs automatically.
  
- **Private Subnet**: 
  - CIDR Block: `10.0.2.0/24`
  - Does not assign public IPs.

### 3. Internet Gateway
- An Internet Gateway is attached to the VPC to allow outbound access from the public subnet.

### 4. Route Tables
- **Public Route Table**:
  - Routes internet traffic to the Internet Gateway.
  
- **Private Route Table**:
  - Routes internet traffic to the NAT Gateway.

### 5. NAT Gateway
- A NAT Gateway is created to allow instances in the private subnet to access the internet while remaining unreachable from outside.

### 6. Security Group
- A Security Group is created to allow SSH access (port 22) only from a specified public IP address, enhancing security.

### 7. EC2 Instance
- An EC2 instance is deployed in the public subnet, configured with the security group.

## CloudFormation Template

The CloudFormation template (`my_cloudformation_template.yaml`) includes the following parameters and resources:

### Parameters
- **MyPublicIP**: Your public IP address (in CIDR notation, e.g., `203.0.113.25/32`) to restrict SSH access.

### Resources
- **VPC**: Creates a new VPC.
- **Public and Private Subnets**: Defines the subnets.
- **Internet Gateway**: Provides internet access.
- **Route Tables**: Configures routing for public and private subnets.
- **NAT Gateway**: Allows outbound internet access for the private subnet.
- **Security Group**: Secures the EC2 instance.
- **EC2 Instance**: The actual compute resource.

## Deployment Steps

1. **Update the Template**:
   - Replace the `ImageId` with your desired AMI ID.
   - Replace `my-key-pair` with the name of your key pair.
   - Specify your public IP address when prompted.

2. **Deploy Using the Script**:
   - Run the `deploy.py` script to create the CloudFormation stack.

3. **Verify Access**:
   - After deployment, use the assigned public IP address to SSH into your EC2 instance.

## Conclusion

This CloudFormation template sets up a secure and efficient network architecture with public and private subnets. It provides a practical example of deploying AWS infrastructure as code.

## License

This project is licensed under the MIT License.
