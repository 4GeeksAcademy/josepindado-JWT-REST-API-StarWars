from .. import db

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    eyes_color = db.Column(db.String(50), default="brown")
    hair_color = db.Column(db.String(50), default="black")

    people = db.relationship('Favourite', backref='people')


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "eyes_color": self.eyes_color,
            "hair_color": self.hair_color
        }
    