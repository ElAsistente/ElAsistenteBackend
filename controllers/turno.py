# -*- coding: utf-8 -*-
# intente algo como
def index():
    grid = SQLFORM.grid(db.turno, user_signature=False)
    return dict(grid=grid)
