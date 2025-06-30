from server.extensions import ma
from server.models.user import User  # Make sure this path is correct
from marshmallow import fields


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True  # If you have foreign keys like orders

    password = fields.String(load_only=True, required=True)
    email = fields.Email(required=True)
    is_admin = fields.Boolean(dump_only=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
