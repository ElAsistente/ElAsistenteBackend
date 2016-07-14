# -*- coding: utf-8 -*-
# intente algo como
def index():
    grid=SQLFORM.grid(db.alumno, user_signature=False,
    links = [lambda row: A(T('Materias'),_href=URL("alumno","view",args=[row.id])), lambda row: A(T('Exámenes'),_href=URL("alumno","examenes",args=[row.id])), lambda row: A(T('Estado Académico'),_href=URL("alumno","estado",args=[row.id]))])
             # lambda row: A(T('Exámenes'),_href=URL("alumno","examenes",args=[row.id]))])
    return dict(grid = grid)

def view():
    id = request.args[0]
    materias= db(db.persona_materia_comision.lista_alumno.belongs(db.alumno.id==id)).select()
    return dict(materias=materias)

def examenes():
    id = request.args[0]
    examenes=db(db.examen_final.alumno==id).select(db.examen_final.fecha_examen, db.examen_final.nota, db.examen_final.materia)
    return dict(examenes=examenes)

def estado():
    id=request.args[0]
    count = db.estado_academico.regulares.count()
    estado=db(((db.alumno.id==id)&(db.auth_user.id==db.alumno.usuario)&(db.estado_academico.usuario==db.auth_user.id))).select(db.estado_academico.usuario, db.estado_academico.regulares.count(), groupby=db.estado_academico.regulares)
    return dict(estado=estado)
