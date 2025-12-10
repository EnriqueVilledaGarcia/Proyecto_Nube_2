from app import db
from datetime import datetime

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    prioridad = db.Column(db.String(20), nullable=False)  # alta, media, baja
    fecha_inicio = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    hora_inicio = db.Column(db.String(5), nullable=True)  # formato HH:MM
    fecha_fin = db.Column(db.DateTime, nullable=True)
    hora_fin = db.Column(db.String(5), nullable=True)  # formato HH:MM
    estatus = db.Column(db.String(20), nullable=False, default='pendiente')  # pendiente, ejecutandose, finalizada