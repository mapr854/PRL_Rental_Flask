from utils.db_sqlite import db

class ElementosContrato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    valor = db.Column(db.Integer,nullable=False )
    cantidad = db.Column(db.Integer)
    contrato_id = db.Column(db.Integer, db.ForeignKey('contrato.id'))
    contrato    = db.relationship('Contrato', back_populates='elementos')
    
    