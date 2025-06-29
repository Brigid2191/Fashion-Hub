from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from server.extensions import db
from server.models.product import Product
from server.schemas.product_schema import product_schema, products_schema

product_bp = Blueprint('products', __name__, url_prefix='/products')

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify(products_schema.dump(products)), 200

@product_bp.route('/', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    errors = product_schema.validates(data)
    if errors:
        return jsonify(errors), 400
    
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return product_schema.jsonify(product), 202

@product_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()

    for key, value in data.items():
        setattr(product, key, value)

    db.session.commit()
    return product_schema.jsonify(product)

@product_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"})
