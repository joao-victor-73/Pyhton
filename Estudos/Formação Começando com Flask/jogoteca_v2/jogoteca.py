from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # pip install flask-SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

# Instanciando a aplicação do SQLAlchemy
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)
