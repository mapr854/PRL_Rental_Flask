from utils.db_sqlite import db

class Parqueadero(db.Model):
    key_id          = db.Column(db.Integer, primary_key = True)
    nplaca         = db.Column(db.String(6), nullable=False)
    place          = db.Column(db.Integer, nullable=False)

    