# -*- coding: utf-8 -*-
@auth.requires_login()
def index():
    table = request.args(0)
    if not table in db.tables(): redirect(URL('error'))
    grid = SQLFORM.grid(db[table],args=request.args[:1] , user_signature=False, csv=true)
    response.title = ' '.join(x.capitalize() for x in table.split('_'))
    return dict(grid = grid)
