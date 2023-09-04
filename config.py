import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DATABASE_NAME = os.getenv("POSTGRES_DB")
DATABASE_USER = os.getenv("POSTGRES_USER")
DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD")

DATABASE_HOST = os.getenv("DJANGO_DATABASE_HOST")
DATABASE_PORT = os.getenv("DJANGO_DATABASE_PORT")
