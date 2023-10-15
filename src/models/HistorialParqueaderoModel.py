from utils.db_sqlite import db

class Parqueadero(db.Model):
    id             = db.Column(db.Integer, primary_key = True)
    nplaca         = db.Column(db.String(6), nullable=False)
    place          = db.Column(db.Integer, nullable=False)
    estado          = db.Column(db.String(1), nullable=False)
    contratos = db.relationship('Contrato', secondary='contrato_parqueadero', back_populates='parqueaderos')

    