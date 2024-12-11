from .. import db

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(100), nullable=True)

    planet = db.relationship('Favorite', backref='planet')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
