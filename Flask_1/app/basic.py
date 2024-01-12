from models import db, Puppy, Owner, Toy

rufus = Puppy("Rufus")
fido = Puppy("Fido")

db.session.add_all([rufus,fido])
db.session.commit()

print(Puppy.query.all())