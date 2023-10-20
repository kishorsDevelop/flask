from database import db, Puppies, app

sam = Puppies('sam', 3)
frank = Puppies('frankie', 4)

with app.app_context():
      db.create_all()
      sam = Puppies('sm', 3)
      frank = Puppies('frank', 4)
      db.session.add_all([sam, frank])
      db.session.commit()
      print(sam.id)
      print(frank.id)

