# -*- coding: utf-8 -*-
# intente algo como
def index():
    grid = SQLFORM.grid(db.detalle_asistencia, user_signature=False)
    return dict(grid=grid)
