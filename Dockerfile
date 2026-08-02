FROM python:3.12
WORKDIR /opt/app
COPY requirements.txt .

RUN pip install -r requirements.txt
