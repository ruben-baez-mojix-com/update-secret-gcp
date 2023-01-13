# Update-secret-gcp

This GitHub action allows you to update secrets on GCP

## Usage

```yml
- name: update secret
  uses: ruben-baez-mojix-com/update-secret-gcp@1.0.0
  with:
    file: env_config
    key: ${{ secrets.SECRET_KEY }}
  env:
    PROJECT_ID: ${{ secrets.PROJECT_ID }}
    SECRET_ID: ${{ secrets.SECRET_ID }}
```

**Required Parameters:**

- `file`: File with secret content to be updated
- `key`: service account to gcp auth

**Environmetal variables:**

- `PROJECT_ID`: GCP project id
- `SECRET_ID`: GCP secret id (name)

### Outputs

- `message`: Result of updated
