from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

c3 = Cupcake(
    flavor="prideful",
    size="extra",
    rating=9.9,
    image="https://images.unsplash.com/photo-1572451479139-6a308211d8be?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTR8fGN1cGNha2V8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
)

db.session.add_all([c1, c2, c3])
db.session.commit()