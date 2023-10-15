from utils.db_sqlite import db


class Cities(db.Model):
    id              =     db.Column(db.Integer, primary_key = True)
    ciudad          = db.Column(db.String(50), nullable=False)
    provincia       = db.Column(db.String(50), nullable=False)
    pais            = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f'{self.ciudad}, {self.provincia}, {self.pais}'