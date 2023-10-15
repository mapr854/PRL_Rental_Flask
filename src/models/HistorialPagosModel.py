from utils.db_sqlite import db

class Pagos(db.Model):
    id              = db.Column(db.Integer, primary_key = True)
    paydate         = db.Column(db.DateTime, nullable=False)
    valor           = db.Column(db.Integer, nullable=False)
    tipo_pago       = db.Column(db.Integer, nullable=False)
    month           = db.Column(db.Integer, nullable=False)
    year            = db.Column(db.Integer, nullable=False)
    contratos       = db.relationship('Contrato', secondary='contrato_pagos', back_populates='pagos')