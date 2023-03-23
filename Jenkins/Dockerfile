FROM python:3.10-slim-buster
WORKDIR /backend
RUN cd ../ && ls
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
