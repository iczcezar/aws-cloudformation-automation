import boto3
import logging

# Configure logging
logging.basicConfig(filename='ec2_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_ec2_instances(state_filter=None):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    
    instances = response['Reservations']
    found_instances = False

    for reservation in instances:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_state = instance['State']['Name']
            instance_type = instance['InstanceType']
            launch_time = instance['LaunchTime']
            tags = instance.get('Tags', [])

            # Convert tags to a dictionary for easier access
            tags_dict = {tag['Key']: tag['Value'] for tag in tags}

            # Filter instances by state if specified
            if state_filter and instance_state != state_filter:
                continue

            found_instances = True
            logging.info(f"Instance ID: {instance_id}, State: {instance_state}, Type: {instance_type}, Launch Time: {launch_time}, Tags: {tags_dict}")

            # Print instance details
            print(f"Instance ID: {instance_id}, State: {instance_state}, Type: {instance_type}, Launch Time: {launch_time}, Tags: {tags_dict}")

            # Alert if instance is stopped
            if instance_state == "stopped":
                print(f"Alert: Instance {instance_id} is stopped!")
                logging.warning(f"Alert: Instance {instance_id} is stopped!")

    if not found_instances:
        print("No EC2 instances found.")
        logging.info("No EC2 instances found.")

if __name__ == "__main__":
    # Optionally filter by state (e.g., "running", "stopped")
    check_ec2_instances(state_filter=None)  # Change None to "running" or "stopped" to filter
