from models import Pet, db
from app import app

db.drop_all()
db.create_all()


fido = Pet(name="Fido", species="cat", available=True)
bowser = Pet(name="bowser", species="dog", age=2, available=True)
spike = Pet(name="spike", species="dog", available=False)

db.session.add(fido)
db.session.add(bowser)
db.session.add(spike)

db.session.commit()
