FROM python:3-slim

RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib google-cloud-secret-manager pydantic
COPY main.py /app/main.py

ENTRYPOINT ["python", "/app/main.py"]