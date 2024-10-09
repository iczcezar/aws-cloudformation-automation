import boto3

def check_ec2_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    
    instances = response['Reservations']
    for reservation in instances:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")

if __name__ == "__main__":
    check_ec2_instances()
