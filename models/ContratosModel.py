from utils.db_sqlite import db



class Contrato(db.Model):
    key_id          = db.Column(db.Integer, primary_key = True)
    contratType     = db.Column(db.String(15), nullable=False)
    precio          = db.Column(db.Integer, nullable=False)
    administracion  = db.Column(db.Integer, nullable=False)
    initialDate     = db.Column(db.DateTime, nullable=False)
    months          = db.Column(db.Integer, nullable=False)
    bono            = db.Column(db.Integer, nullable=False)
    poliza          = db.Column(db.String(50), nullable=False)


    # Relación con Inmueble
    inmueble        = db.relationship('Inmueble', back_populates='contrato')


    # Relación con Arrendador
    arrendador_id = db.Column(db.Integer, db.ForeignKey('arrendador.key_id'))
    arrendador = db.relationship('Arrendador', back_populates='contratos')


    # Relación con Arrendatario
    arrendatarios = db.relationship('Arrendatario', secondary='contrato_arrendatario', back_populates='contratos')


    # Relación con Parqueaderos
    parqueaderos = db.relationship('Parqueadero', secondary='contrato_parqueadero', back_populates='contratos')


    # Relación con Elementos de Inventario
    elementos_contrato = db.relationship('ElementoContrato', back_populates='contrato')

    # Relación con Pagos
    pagos = db.relationship('Pagos', secondary='contrato_pagos', back_populates='contratos')
    

             

   


