import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv 

#Cargar las variables de entorno
load_dotenv()

#crear instancia
app =  Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Importar modelos para que SQLAlchemy los reconozca
from app.models import Tarea

# Importar y registrar blueprints
from app.routes.tarea import tarea_bp

# Crear las tablas si no existen
with app.app_context():
    db.create_all()
    
app.register_blueprint(tarea_bp, url_prefix='/tareas')


#Ruta principal home
@app.route('/')
def index():
    tareas = Tarea.query.all()
    return render_template('index.html', tareas=tareas)