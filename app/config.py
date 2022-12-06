import os
from dotenv import load_dotenv

class Config:
    # Database configuration
    DB_HOST = os.environ.get('DB_HOST') or 'db'
    DB_USER = os.environ.get('DB_USER') or 'root'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'mysql'
    DB_NAME = os.environ.get('DB_NAME') or 'myapp'
    # Secret Key for application
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess'
