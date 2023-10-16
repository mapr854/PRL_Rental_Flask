from utils.db_sqlite import db
from sqlalchemy import Table, Column, Integer, ForeignKey

# Tabla intermedia para la relación muchos a muchos entre Contrato y Arrendatario
contrato_arrendatario = db.Table('contrato_arrendatario',
    db.Column('contrato_id', db.Integer, db.ForeignKey('contrato.id')),
    db.Column('arrendatario_id', db.Integer, db.ForeignKey('arrendatario.id'))
)



# Tabla intermedia para la relación muchos a muchos entre Contrato y Parqueadero
contrato_parqueadero = db.Table('contrato_parqueadero',
    db.Column('contrato_id', db.Integer, db.ForeignKey('contrato.id')),
    db.Column('parqueadero_id', db.Integer, db.ForeignKey('parqueadero.id'))
)



# Tabla intermedia para la relación muchos a muchos entre Contrato y Pagos
contrato_pagos = db.Table('contrato_pagos',
    db.Column('contrato_id', db.Integer, db.ForeignKey('contrato.id')),
    db.Column('pagos_id', db.Integer, db.ForeignKey('pagos.id'))
)