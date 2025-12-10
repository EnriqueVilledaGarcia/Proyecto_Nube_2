from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Tarea
from datetime import datetime

tarea_bp = Blueprint('tareas', __name__)

@tarea_bp.route('/')
def listar_tareas():
    tareas = Tarea.query.all()
    return render_template('index.html', tareas=tareas)

@tarea_bp.route('/nuevo', methods=['GET', 'POST'])
def nueva_tarea():
    if request.method == 'POST':
        nombre = request.form['nombre']
        prioridad = request.form['prioridad']
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d') if request.form['fecha_inicio'] else datetime.utcnow()
        hora_inicio = request.form.get('hora_inicio', '')
        fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d') if request.form['fecha_fin'] else None
        hora_fin = request.form.get('hora_fin', '')
        estatus = request.form.get('estatus', 'pendiente')
        
        nueva = Tarea(
            nombre=nombre,
            prioridad=prioridad,
            fecha_inicio=fecha_inicio,
            hora_inicio=hora_inicio if hora_inicio else None,
            fecha_fin=fecha_fin,
            hora_fin=hora_fin if hora_fin else None,
            estatus=estatus
        )
        db.session.add(nueva)
        db.session.commit()
        return redirect(url_for('tareas.listar_tareas'))
    return render_template('form.html')
