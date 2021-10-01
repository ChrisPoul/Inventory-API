import os

db_dialect = os.environ.get('DB_DIALECT', default='mysql')
db_host = os.environ.get('DB_HOST', default='localhost')
db_name = os.environ.get('DB_NAME', default='EnGo_db')
db_user = os.environ.get('DB_USERNAME', default='admin')
db_password = os.environ.get('DB_PASSWORD', default='')
db_port = os.environ.get('DB_PORT', default='3306')

SQLALCHEMY_DATABASE_URI = f"{db_dialect}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
