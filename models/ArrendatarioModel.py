from utils.db_sqlite import db

class Arrendatario(db.Model):
    key_id          = db.Column(db.Integer, primary_key = True)
    tipoid          = db.Column(db.String(10), nullable=False)
    idnumber        = db.Column(db.Integer, unique = True, nullable=False)
    estado          = db.Column(db.String(1), nullable=False)
    nombres         = db.Column(db.String(100), nullable=False)
    apellidos       = db.Column(db.String(100), nullable=False)
    email           = db.Column(db.String(100), nullable=False)
    movil           = db.Column(db.Integer, nullable=False)
    fechaNacimiento = db.Column(db.DateTime, nullable=False)
    pais_exp        = db.Column(db.String(50), nullable=False)
    provincia_exp   = db.Column(db.String(50))
    ciudad_exp      = db.Column(db.String(50))
    nombreContacto  = db.Column(db.String(100))
    movil           = db.Column(db.Integer)
    profesion       = db.Column(db.String(100))
    contratos       = db.relationship('Contrato', secondary='contrato_arrendatario', back_populates='arrendatarios')
    

