from server.extensions import ma
from server.models.order import Order


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        include_fk = True

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
