# -*- coding: utf-8 -*-
@auth.requires_login()
def index():
    lista = []
    for table in db.tables():
        lista.append(A(_href=URL("tabla", args=[table])))
    return dict(tablas= lista)

def tabla():
    table = request.args(0)
    if not table in db.tables(): redirect(URL('error'))
    grid = SQLFORM.grid(db[table],args = request.args[:1] , user_signature=False, csv=True)
    response.title = ' '.join(x.capitalize() for x in table.split('_'))
    return dict(grid = grid)
