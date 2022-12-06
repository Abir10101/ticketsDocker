FROM python:3.7.15-alpine3.17
WORKDIR /backend
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["sh", "run.sh"]