import boto3
import json

# Configuration
STACK_NAME = 'MyEC2Stack'
TEMPLATE_FILE = '../templates/my_cloudformation_template.yaml'

def load_template():
    with open(TEMPLATE_FILE) as template_file:
        return template_file.read()

def create_stack(cloudformation_client):
    template_body = load_template()
    response = cloudformation_client.create_stack(
        StackName=STACK_NAME,
        TemplateBody=template_body,
        Capabilities=['CAPABILITY_IAM'],  # If your template uses IAM resources
    )
    return response

def main():
    cloudformation_client = boto3.client('cloudformation', region_name='us-east-1')  # Change the region as needed
    response = create_stack(cloudformation_client)
    print(f'Stack creation initiated: {response["StackId"]}')

if __name__ == '__main__':
    main()
