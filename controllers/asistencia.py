# -*- coding: utf-8 -*-
# intente algo como
def index():
    grid=SQLFORM.grid(db.asistencia, user_signature=False,
    links = [lambda row: A(T('Planilla'),_href=URL("asistencia","view",args=[row.id]))])
    return dict(grid = grid)

def view():
    id = request.args[0]
    asistencia=db(((db.asistencia.id==id)&(db.materia_comision_ciclo.id==db.asistencia.materia_comision_ciclo)& (db.persona_materia_comision.materia_comision_ciclo==db.materia_comision_ciclo.id)&(db.alumno.id==db.persona_materia_comision.lista_alumno))).select(db.alumno.legajo, db.alumno.apellido, db.alumno.nombre)
    return dict(asistencia=asistencia)
