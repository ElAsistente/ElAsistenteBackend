# -*- coding: utf-8 -*-
# intente algo como
def index():
    grid = SQLFORM.grid(db.modulo, user_signature=False)
    return dict(grid=grid)
