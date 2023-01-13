import argparse
import os
import sys
from google.cloud import secretmanager
from google.oauth2 import service_account


def main(filename, project_id, secret_id, keyfile):
    credentials = service_account.Credentials.from_service_account_file(keyfile)
    with open(filename, 'rb') as file:
        print(f"Updating {filename}..")
        data = file.read()
        client = secretmanager.SecretManagerServiceClient(credentials=credentials)
        parent = client.secret_path(project_id, secret_id)
        response = client.add_secret_version(
            request={"parent": parent, "payload": {"data": data}}
        )
        print(f"::set-output name=message::{response}")
        return response


if __name__ == '__main__':
    #Get args
    parser = argparse.ArgumentParser(description="Update secret")
    parser.add_argument('file')
    filename = parser.parse_args().file
    key = argparse.ArgumentParser(description="Application credentials")
    key.add_argument('key')
    keyfile = key.parse_args().key
    project_id = os.getenv("PROJECT_ID")
    secret_id = os.getenv("SECRET_ID")

    #Validating file
    if not os.path.exists(filename):
        print(f"ERROR: file {filename} doesn't exist")
        sys.exit(1)
    if not os.path.exists(keyfile):
        print(f"ERROR: key {keyfile} doesn't exist")
        sys.exit(1)

    main(filename, project_id, secret_id, keyfile)

