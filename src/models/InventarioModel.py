from utils.db_sqlite import db

class Inventario(db.Model):
    id              = db.Column(db.Integer, primary_key = True)
    descripcion     = db.Column(db.String(200), nullable=False)
    valor          = db.Column(db.Integer, nullable=False)
    estado         = db.Column(db.String(200), nullable=False)

class ElementoContrato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)

    # Relación con Contrato
    contrato_id = db.Column(db.Integer, db.ForeignKey('contrato.id'))
    contrato = db.relationship('Contrato', back_populates='elementos_contrato')

    # Relación con ElementoInventario
    inventario_id = db.Column(db.Integer, db.ForeignKey('inventario.id'))
    inventario = db.relationship('Inventario')
    