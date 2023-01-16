# Update-secret-gcp

This GitHub action allows you to update secrets on GCP

## Usage

```yml
- name: update secret
  uses: ruben-baez-mojix-com/update-secret-gcp@v1.0.0
  with:
    path: config/config.json
  env:
    PROJECT_ID: ${{ secrets.PROJECT_ID }}
    SECRET_ID: ${{ secrets.SECRET_ID }}
    KEYFILE: ${{ secrets.SERVICE_ACCOUNT }}
```

**Required Parameters:**

- `path`: File with secret content to be updated

**Environmetal variables:**

- `PROJECT_ID`: GCP project id
- `SECRET_ID`: GCP secret id (name)
- `KEYFILE`: service account to gcp auth

### Outputs

- `message`: Result of updated
