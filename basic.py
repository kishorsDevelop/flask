from models import db, app, Puppy, Owner, Toy

with app.app_context():
   
    db.create_all()
    
    # rufus = Puppy('rufus')
    # fido = Puppy('fido')
    
    # db.session.add_all([rufus, fido])
    # db.session.commit()

    rufus = Puppy.query.filter_by(name='rufus').first()
    # print(rufus)
    josh = Owner('josh', rufus.id)
    
    toy1 = Toy('Chew toy', rufus.id)
    toy2 = Toy('Ball', rufus.id)

    db.session.add_all([josh, toy1, toy2])
    db.session.commit()

    rufus = Puppy.query.filter_by(name='rufus').first()
    rufus.report_toys()