import os

MONGODB_SETTINGS = dict(
    db=os.environ.get('DB_NAME', default='Inventory_db'),
    host=os.environ.get('DB_HOST', default='localhost'),
    port=int(os.environ.get('DB_PORT', default=27017)),
    username=os.environ.get('DB_USERNAME', default=''),
    password=os.environ.get('DB_PASSWORD', default='')
)
