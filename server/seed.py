from faker import Faker
from run import create_app
from server.extensions import db  
from server.models.product import Product

fake = Faker()
app = create_app()

with app.app_context():
    print("🔁 Seeding data with Faker...")

    # Clear existing data
    Product.query.delete()

    # Create fake products
    products = []  
    for _ in range(20):
        product = Product(
            name=fake.word().capitalize() + " " + fake.word().capitalize(),
            price=round(fake.random_number(digits=4) / 100, 2),
            description=fake.sentence(nb_words=6),
            stock=fake.random_int(min=1, max=50)
        )
        products.append(product)  

    # Add and commit
    db.session.add_all(products)
    db.session.commit()

    print("✅ Done seeding with Faker!")
