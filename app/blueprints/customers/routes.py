
from app.blueprints.customers import customers_bp

from .schemas import customer_schema, customers_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Customers, db
from sqlalchemy import select





@customers_bp.route("/", methods =['POST'])
def create_customer():
    try: # validation error, this type of error handling, handles commands that isnt recognizable 
        customer_data = customer_schema.load(request.json) # command this is to load only validate information
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_customer = Customers(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])
    db.session.add(new_customer) # add to session
    db.session.commit() #upload info to database

    return jsonify("Customer has been added our database."), 201


@customers_bp.route("/", methods =['GET'])
def get_customers():
    query = select(Customers)
    customers = db.session.execute(query).scalars().all()

    return customers_schema.jsonify(customers), 200





@customers_bp.route ("/<int:customer_id>", methods=['GET'])
def get_customer(customer_id):
    customer = db.session.get(Customers, customer_id )

    return customer_schema.jsonify(customer), 200


@customers_bp.route("/<int:customer_id>", methods =['PUT'])
def update_customer(customer_id):
    customer = db.session.get(Customers, customer_id)

    if customer == None:
        return jsonify ({"message": "invalid id"}), 400
    
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    for field, value in customer_data.items():
        if value:
            setattr(customer, field, value)

    db.session.commit()
    return customer_schema.jsonify(customer), 200



@customers_bp.route("/<int:customer_id>", methods=['DELETE'])
def delete_customer(customer_id):
    customer = db.session.get(Customers, customer_id)

    if customer == None:
        return jsonify({"message": "invalid id"}), 400

    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": f"User at ID {customer_id}  has been deleted "})
