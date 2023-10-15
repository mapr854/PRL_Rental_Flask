from utils.db_sqlite import db


class Arrendador(db.Model):
    key_id          = db.Column(db.Integer, primary_key = True)
    tipoid          = db.Column(db.String(10), nullable=False)
    idnumber        = db.Column(db.Integer, unique = True, nullable = False)
    nombres         = db.Column(db.String(100), nullable=False)
    estado          = db.Column(db.String(1), nullable=False)
    apellidos       = db.Column(db.String(100), nullable=False)
    email           = db.Column(db.String(100), nullable=False)
    movil           = db.Column(db.Integer, nullable=False)
    pais_exp        = db.Column(db.String(50), nullable=False)
    provincia_exp   = db.Column(db.String(50))
    ciudad_exp      = db.Column(db.String(50))
    contratos = db.relationship('Contrato', back_populates='arrendador')

    


