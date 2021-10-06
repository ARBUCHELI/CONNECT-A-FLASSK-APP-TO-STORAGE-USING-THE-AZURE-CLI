import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'bucheli-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'bucheli-database'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'buchenadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'RothWulf@1977'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'buchenstorage12'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'yyLO3FzpoIjXGG49op/2RR9/V8Mhh19TaBtGUJ0NP2+RMJ2fqaCogBjiQKXPhOOjFBsZJyxcTo4U9v8P9qqDUg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
