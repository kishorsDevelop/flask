from db import db, Puppy

## CREATE ##
my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()

## READ ##
all_puppies = Puppy.query.all() #list of puppies in table
#print(all_puppies)

# SELECT BY ID
puppy_one = db.session.get(Puppy,3)
print(puppy_one.name)

## FILTER ##
puppy_frankie = Puppy.query.filter_by(name='Frankie')
#print(puppy_frankie.all())

## UPDATE ##
first_puppy = db.session.get(Puppy,3)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

## DELETE ##
first_pup = db.session.get(Puppy,1)
db.session.delete(first_pup)
db.session.commit()

all_puppies = Puppy.query.all()
#print(all_puppies)