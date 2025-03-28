from os import environ

from dotenv import load_dotenv

load_dotenv()

# print(environ)


class Config:
    # General pattern
    # mssql+pyodbc://<username>:<password>@<dsn_name>?driver=<driver_name>
    # mssql+pyodbc://@<server_name>/<db_name>?driver=<driver_name>
    # connection string ⬇️
    SQLALCHEMY_DATABASE_URI = environ.get("LOCAL_DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
