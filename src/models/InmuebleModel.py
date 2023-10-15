from utils.db_sqlite import db

class Inmueble(db.Model):
    id              = db.Column(db.Integer, primary_key = True)
    name            = db.Column(db.String(10), unique = True, nullable=False)
    estado          = db.Column(db.String(1), nullable=False)
    direccion       = db.Column(db.String(200), nullable=False)
    ciudad          = db.Column(db.String(50), nullable=False)
    tipo            = db.Column(db.String(15), nullable=False)
    Apartamento     = db.Column(db.Integer, nullable=False)
    habitaciones    = db.Column(db.Integer, nullable=False)
    banos           = db.Column(db.Integer)
    cod_gas         = db.Column(db.Integer)
    cod_luz         = db.Column(db.Integer)
    cod_agua        = db.Column(db.Integer)
    contrato_id     = db.Column(db.Integer, db.ForeignKey('contrato.id'))
    contratos        = db.relationship('Contrato', back_populates='inmueble')
    