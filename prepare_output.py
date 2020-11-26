import os
import boto3
import json
import logging
import sys

REGION = os.getenv('REGION', 'us-west-2')
STACK_NAME = os.getenv('STACK_NAME', 'temp-stack')

if not STACK_NAME and not REGION:
    logging.error('Required environment variables not set. Exiting.')
    sys.exit(1)

def get_client(region):
    return boto3.client('cloudformation', region)

def create_output(stack_name, client):
    resources = {}
    try:
        response = client.describe_stack_resources(
            StackName=stack_name
        )
        for resource in response['StackResources']:
            resources[resource['LogicalResourceId']] = resource['PhysicalResourceId']
        with open('output.json', 'w') as out_obj:
            out_obj.write(json.dumps(resources, indent=2))
        logging.info('Created resource output file for stack: {}'.format(stack_name))
    except Exception as error:
        logging.error(error)

def main():
    cf_client = get_client(REGION)
    create_output(STACK_NAME, cf_client)

if __name__ == '__main__':
    main()