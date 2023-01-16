import os
import sys
import json
import base64
from google.cloud import secretmanager
from google.oauth2 import service_account


def main(path, project_id, secret_id, keyfile):
    decoded_key = base64.b64decode(keyfile)
    decoded_str = decoded_key.decode("ascii")
    final_key = json.loads(decoded_str)
    credentials = service_account.Credentials.from_service_account_info(final_key)
    with open(path, 'rb') as file:
        print(f"Updating {path}..")
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
    path = os.environ["INPUT_PATH"]

    project_id = os.getenv("PROJECT_ID")
    secret_id = os.getenv("SECRET_ID")
    keyfile = os.getenv("KEYFILE")

    main(path, project_id, secret_id, keyfile)

