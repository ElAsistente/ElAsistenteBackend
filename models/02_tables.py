db.define_table('alumno',
                Field('legajo', 'integer', label = 'Legajo'),
                Field('apellido', 'text', label = 'Apellido'),
                Field('nombre', 'text', label = 'Nombre'),
                Field('foto', 'upload', label = 'Foto'),
                Field('email', 'string', label = 'E-mail'),
                Field('usuario',db.auth_user, default=auth.user_id, readable=True, writable=False),
                format = '%(nombre)s %(apellido)s')

db.define_table('bedel',
                Field('legajo', 'integer', label = 'Legajo'),
                Field('apellido', 'text', label = 'Apellido'),
                Field('nombre', 'text', label = 'Nombre'),
                Field('email', 'string', label = 'E-mail'),
                Field('usuario',db.auth_user, default=auth.user_id, readable=True, writable=False),
                format = '%(nombre)s %(apellido)s')

db.define_table('profesor',
                Field('legajo', 'integer', label = 'Legajo'),
                Field('nombre', 'string', label = 'Nombre'),
                Field('apellido', 'string', label = 'Apellido'),
                Field('email', 'string', label = 'Email'),
                Field('foto', 'upload', label = 'Foto'),
                Field('usuario',db.auth_user, default=auth.user_id, readable=True, writable=False),
                format = '%(nombre)s %(apellido)s')

db.define_table('turno',
                Field('descripcion', requires=IS_IN_SET(['Mañana','Tarde','Noche']), length=15),
                Field('numero_turno', requires=IS_IN_SET(['0','1','2']), length=2),
                format='%(descripcion)s'
               )

db.define_table('modulo',
                Field('turno', db.turno),
                Field('hora_inicio', type='time' ,label="Hora de Inicio"),
                Field('hora_fin', type='time' ,label="Hora de Finalización"),
                Field('numero_modulo', requires=IS_IN_SET(['-1','0','1','2','3','4','5','6','7']), length=3),
                format='%(hora_inicio)s'
               )

db.define_table('comision',
                Field('nombre' , 'string' ,  label = 'Nombre'),
                Field('turno' , 'reference turno' ,  label = 'Turno'),
                Field('modulo' , 'reference modulo' ,  label = 'Módulo'),
                Field('nivel' , 'integer' , label = 'Nivel'),
                format = '%(nombre)s')

db.define_table('materia',
                Field('nivel', widget=SQLFORM.widgets.radio.widget, requires=IS_IN_SET(['1', '2', '3', '4', '5']), label='Nivel'),
                Field('nombre', length=200),
                Field('carga_anual', label='Carga Horaria Anual', length=20),
                Field('primer_cuatrimestre', label='Carga Horaria 1C', length=20),
                Field('segundo_cuatrimestre', label='Carga Horaria 2C', length=20),
                format='%(nombre)s'
               )

db.define_table('parcial',
                Field('fecha_examen', 'date', label = 'Fecha del parcial'),
                Field('nota', requires=IS_IN_SET(['1','2','3','4','5','6','7','8','9','10']), label='Nota'),
                Field('alumno', 'reference alumno', label = 'Alumno'),
                Field('materia', 'reference materia', label = 'Materia'),
                Field('comision', 'reference comision', label = 'Comisión'),
                Field('profesor', 'reference profesor', label = 'Profesor'),
                )

db.define_table('examen_final',
                Field('fecha_examen', 'date', label = 'Fecha del final'),
                Field('nota', requires=IS_IN_SET(['1','2','3','4','5','6','7','8','9','10']), label='Nota'),
                Field('alumno', 'reference alumno', label = 'Alumno'),
                Field('materia', 'reference materia', label = 'Materia'),
                Field('profesor', 'reference profesor', label = 'Profesor'),
                )

db.define_table('estado_academico',
                Field('usuario',db.auth_user, default=auth.user_id, readable=True, writable=False),
                Field('regulares','list:reference materia', label='Regulares', widget=SQLFORM.widgets.checkboxes.widget),
                Field('aprobadas','list:reference materia', label='Aprobadas', widget=SQLFORM.widgets.checkboxes.widget),
               )

db.define_table('correlativa',
                Field('materia', db.materia),
                Field('rpc','list:reference materia', label='Regulares para Cursar', widget=SQLFORM.widgets.checkboxes.widget),
                Field('apc','list:reference materia', label='Aprobadas para Cursar', widget=SQLFORM.widgets.checkboxes.widget),
                )

db.define_table('aula',
                Field('numero', 'integer', label = 'Numero'),
                Field('capacidad', 'integer', label = 'Capacidad'),
                Field('estado', requires=IS_IN_SET( ['Ocupada' ,'Libre' ,'Reservada'])),
                Field('responsable', 'reference profesor' , label = 'Responsable'),
                Field('comision', 'reference comision', label = 'Comisión'),
                Field('materia', 'reference materia', label = 'Materia'),
                format = '%(numero)s')

db.define_table('materia_comision_ciclo',
                Field('ciclo', 'integer', label = 'Ciclo Lectivo'),
                Field('descripcion_materiacomision', 'string', label = 'Descripción'),
                Field('materia', 'reference materia', label = 'Materia'),
                Field('comision','reference comision', label = 'Comisión'),
                Field('profesor', 'reference profesor', label = 'Profesor'),
                format = '%(descripcion_materiacomision)s'
                )

db.define_table('persona_materia_comision',
                Field('materia_comision_ciclo','reference materia_comision_ciclo', label = 'Materia, comisión y Ciclo Lectivo'),
                Field('lista_alumno','reference alumno', label = 'Alumnos'),
                )

db.define_table('horario_clases',
                Field('turno', db.turno),
                Field('materia', db.materia, label='Materia'),
                Field('comision', requires=IS_IN_SET(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']), label='Comisión', length=3),
                Field('dia', requires=IS_IN_SET(['1', '2', '3', '4', '5']), label='Día', length=2),
                Field('modulo','list:reference modulo', label='Módulo', widget=SQLFORM.widgets.checkboxes.widget)
               )

db.define_table('franja_horaria',
                Field('usuario',db.auth_user, default=auth.user_id, readable=True, writable=False),
                Field('diamodulo'),
               )

db.define_table('asistencia',
                Field('fecha', 'date', label = 'Fecha'),
                Field('ciclo', 'integer', label = 'Ciclo Lectivo'),
                Field('materia_comision_ciclo', 'reference materia_comision_ciclo', label = 'Materia, Comisión y Ciclo'),
                Field('profesor', 'reference profesor', label = 'Profesor'),
                )

db.define_table('detalle_asistencia',
                Field('alumno', 'reference alumno', label = 'Alumno'),
                Field('comision' , 'reference comision' , label = 'Comisión' ),
                Field('materia', 'reference materia', label = 'Materia'),
                Field('id_asistencia','reference asistencia', label = 'Planilla'),
                Field('estado' , requires=IS_IN_SET(['Presente' , 'Ausente']) ),
                )
