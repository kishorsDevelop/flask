from my_project import db
class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    pup_id = db.Column(db.Integer, db.ForeignKey('puppy.id'))
    
    def __init__(self, name, id):
        self.name = name
        self.pup_id = id
    
    def __repr__(self):
        return f"Owner Name: {self.name}"

class Puppy(db.Model):
    __tablename__ = 'puppy'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='Puppy', uselist=False)

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        return f"Puppy name: {self.name} and now owner assigned yet!"
