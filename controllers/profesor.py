# -*- coding: utf-8 -*-
# intente algo como
def index():
    grid=SQLFORM.grid(db.profesor, user_signature=False,
    links = [lambda row: A(T('Materias'),_href=URL("profesor","view",args=[row.id])), lambda row: A(T('Temario'),_href=URL("profesor","temas",args=[row.id]))])
    return dict(grid = grid)

def view():
   id = request.args[0]
   materias= db(db.materia_comision_ciclo.profesor.belongs(db.profesor.id==id)).select()
   return dict(materias=materias)

def temas():
    import datetime
    hoy = datetime.datetime.today()
    id = request.args[0]
    temas= db((db.tema.profesor==id)&(db.tema.fecha==hoy)).select(db.tema.titulo, db.tema.descripcion, db.tema.materia)
    return dict(temas=temas)
