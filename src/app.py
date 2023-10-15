from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from routes import *
import pandas as pd
from utils.db_sqlite import db

app = Flask(__name__)

db_path = os.path.join(app.root_path, 'database', 'rentalmanagment2.db')
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from models import Cities


app.register_blueprint(admin_bp)
app.register_blueprint(arrendador_bp,url_prefix='/arrendador')
app.register_blueprint(arrendatario_bp,url_prefix='/arrendatario')


db.configure_mappers()

with app.app_context():
    print("Entering app context...")
    db.create_all()
    print("Tables created successfully.")
    print("Exiting app context...")


