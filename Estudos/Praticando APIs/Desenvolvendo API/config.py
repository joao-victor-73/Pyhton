DEBUG = True

# Banco de dados
USERNAME = 'root'
PASSWORD = 'darc147'
SERVER = 'localhost'
DB = 'api_flask'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True