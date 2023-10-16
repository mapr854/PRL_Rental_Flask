from utils.db_sqlite import db

class Inmueble(db.Model):
    key_id          = db.Column(db.Integer, primary_key = True)
    name            = db.Column(db.String(10), unique = True, nullable=False)
    direccion       = db.Column(db.String(200), nullable=False)
    ciudad          = db.Column(db.String(50), nullable=False)
    tipo            = db.Column(db.String(15), nullable=False)
    habitaciones    = db.Column(db.Integer, nullable=False)
    contratos        = db.relationship('Contrato', back_populates='inmueble')
    