from server.extensions import ma
from server.models.product import Product


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        include_fk = True  # Optional if you have foreign keys

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
