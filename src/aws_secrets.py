import boto3
import secrets

client = boto3.client("secretsmanager", region_name="us-east-1")

def get_secret(name: str):
    response = client.get_secret_value(SecretId=name)
    return response["SecretString"]

def rotate_secret(name: str):
    new_value = secrets.token_urlsafe(32)
    client.put_secret_value(SecretId=name, SecretString=new_value)
    return new_value