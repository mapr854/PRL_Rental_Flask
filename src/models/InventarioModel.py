from utils.db_sqlite import db


class Inventario(db.Model):
    id              = db.Column(db.Integer, primary_key = True)
    descripcion     = db.Column(db.String(200), nullable=False)
    valor          = db.Column(db.Integer, nullable=False)
    estado         = db.Column(db.String(200), nullable=False)

    