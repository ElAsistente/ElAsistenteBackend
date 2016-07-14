# -*- coding: utf-8 -*-
# intente algo como
def index():
 grid = SQLFORM.grid(db.persona_materia_comision, user_signature=False)
 return dict(grid = grid)
