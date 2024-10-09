# AWS Resource Monitoring Automation

This project automates the monitoring of AWS resources using Python and AWS services. It checks the status of various resources, including EC2 instances, S3 buckets, and RDS databases, and sends alerts based on predefined conditions.

## Features
- Monitors key metrics (e.g., CPU usage, storage levels) for AWS resources.
- Utilizes AWS Lambda for serverless execution of monitoring scripts.
- Integrates with Amazon CloudWatch for real-time monitoring and alerts.
- Sends notifications via Amazon SNS for important events (e.g., high CPU usage, untagged resources).
- Provides logging and reporting for historical reference.

## Technologies Used
- **Python**
- **Boto3** (AWS SDK for Python)
- **AWS Lambda**
- **Amazon CloudWatch**
- **Amazon SNS**
- **AWS IAM**

## Getting Started
1. Clone the repository.
   ```bash
   git clone https://github.com/AWSPyDev/aws-resource-monitor.git
2. Set up your AWS credentials.
3. Deploy the Lambda function and configure CloudWatch Events.
4. Customize monitoring conditions as needed.

## Contributing
Feel free to submit issues or pull requests to enhance this project!

## License
This project is licensed under the MIT License - see the LICENSE file for details.



