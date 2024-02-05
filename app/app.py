#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Restaurant, Restaurant_pizza, Pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return  "<h1>Pizzas</h1>"

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()

    result = [
        {"id": restaurant.id , "name": restaurant.name, "address": restaurant.address}
        for restaurant in restaurants
    ]
    

    response = make_response(jsonify(result))
    

    return response
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()

    if pizzas:
        response = [ {"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in pizzas]
        
        return jsonify(response)
    else:
        return "Pizza unavailable"
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    
    if restaurant:
        result = {
            "id": restaurant.id, "name": restaurant.name , "address": restaurant.address ,
            "pizzas": [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in restaurant.pizzas], 
        }
        response = jsonify(result)

        return response
    else:
        result = "Restaurant not found", 404 
        response = jsonify(result)

        return response
    
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)

    if restaurant:
        Restaurant_pizza.query.filter_by(restaurant_id=id).delete()
        db.session.delete(restaurant)
        db.session.commit()

        return jsonify({'message': 'Restaurant deleted successfully'}, 204)

    else:
        response= jsonify({"error": "No such restaurant"})

        return response

@app.route('/Restaurant_pizzas', methods=['POST'])
def post_restaurant():
    data = request.get_json()
    if data:
        pizzas = Restaurant_pizza(price=data['price'], pizza_id=data['pizza_id'], restaurant_id=data['restaurant_id'])
        db.session.add(pizzas)
        db.session.commit()
        pizza = Pizza.query.get(data['pizza_id'])
        return jsonify({"id":pizza.id, "name":pizza.name, "ingredients": pizza.ingredients})
    else:
        response = ({"error": ["Validation errors"]}, 400)

        return jsonify(response)
    


if __name__ == '__main__':
    app.run(port=5001 , debug=True)

