from database import app, db, Puppies

with app.app_context():
    # CREATE #

    puppy = Puppies('rufus', 5)
    db.session.add(puppy)
    db.session.commit()

    # READ #

    all_puppies = Puppies.query.all()
    print(all_puppies)

    # SELECT BY ID #

    puppy_1 = Puppies.query.get(1)
    print(puppy_1.name)

    # FILTERS #

    puppy_franky = Puppies.query.filter_by(name='frank')
    print(puppy_franky.all())

    # UPDATE #

    second_puppy = Puppies.query.get(2)
    second_puppy.name = 'tommy'
    db.session.add(second_puppy)
    db.session.commit()

    # DELETE #

    puppy_3 = Puppies.query.get(4)
    db.session.delete(puppy_3)
    db.session.commit()

    # PRINTING #

    all_puppies = Puppies.query.all()
    print(all_puppies)

