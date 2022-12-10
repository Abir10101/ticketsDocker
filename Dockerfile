FROM python:3.10-alpine
WORKDIR /backend
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["sh", "run.sh"]