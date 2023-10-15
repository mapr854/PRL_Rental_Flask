from utils.db_sqlite import db



class Contrato(db.Model):
    id              = db.Column(db.Integer, primary_key = True)
    contractType     = db.Column(db.String(15), nullable=False)
    precio          = db.Column(db.Integer, nullable=False)
    administracion  = db.Column(db.Integer, nullable=False)
    startDate       = db.Column(db.DateTime, nullable=False)
    endDate         = db.Column(db.DateTime, nullable=True)
    months          = db.Column(db.Integer, nullable=False)
    bono            = db.Column(db.Integer, nullable=False)
    poliza          = db.Column(db.String(50), nullable=False)
    estado          = db.Column(db.String(1), nullable=False)


    # Relación con Inmueble
    
    inmueble_id = db.Column(db.Integer, db.ForeignKey('inmueble.id'))
    inmueble        = db.relationship('Inmueble', back_populates='contratos')

    # Relación con Arrendador
    arrendador_id = db.Column(db.Integer, db.ForeignKey('arrendador.id'))
    arrendador = db.relationship('Arrendador', back_populates='contratos')


    # Relación con Arrendatario
    arrendatarios = db.relationship('Arrendatario', secondary='contrato_arrendatario', back_populates='contratos')
    

    # Relación con Parqueaderos
    parqueaderos = db.relationship('Parqueadero', secondary='contrato_parqueadero', back_populates='contratos')


    # Relación con Elementos de Inventario
    elementos_contrato = db.relationship('ElementoContrato', back_populates='contrato')

    # Relación con Pagos
    pagos = db.relationship('Pagos', secondary='contrato_pagos', back_populates='contratos', lazy='dynamic')
    

             

   


