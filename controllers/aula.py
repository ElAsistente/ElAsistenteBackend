# -*- coding: utf-8 -*-
# intente algo como
def index():
    grid=SQLFORM.grid(db.aula, user_signature=False)
    return dict(grid=grid)

def listado():
    listado=db(db.aula.estado=='Libre').select(db.aula.numero, db.aula.capacidad, db.aula.estado)
    return dict(listado=listado)
