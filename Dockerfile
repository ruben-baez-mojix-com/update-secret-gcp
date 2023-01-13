FROM python:3-slim

RUN pip install -r requirements.txt
COPY main.py /app/main.py

ENTRYPOINT ["python", "/app/main.py"]