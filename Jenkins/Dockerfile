FROM python:3.10-alpine
WORKDIR /backend
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

FROM mysql:8.0.31
WORKDIR /docker-entrypoint-initdb.d
ENV MYSQL_ROOT_PASSWORD admin
ENV MYSQL_DATABASE myapp
# COPY ../database/* .
