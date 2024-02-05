from app import app, db
from models import Restaurant, Pizza, Restaurant_pizza

with app.app_context():
    # Seed Restaurants
    restaurant1 = Restaurant(name='Pizza Palace')
    restaurant2 = Restaurant(name='Italian Delight')
    db.session.add_all([restaurant1, restaurant2])
    db.session.commit()

    # Seed Pizzas
    pizza1 = Pizza(name='Margherita')
    pizza2 = Pizza(name='Pepperoni Lovers')
    pizza3 = Pizza(name='Vegetarian')
    db.session.add_all([pizza1, pizza2, pizza3])
    db.session.commit()

    # Seed RestaurantPizzas
    restaurant_pizza1 = Restaurant_pizza(restaurant_id=restaurant1.id, pizza_id=pizza1.id)
    restaurant_pizza2 = Restaurant_pizza(restaurant_id=restaurant1.id, pizza_id=pizza2.id)
    restaurant_pizza3 = Restaurant_pizza(restaurant_id=restaurant2.id, pizza_id=pizza2.id)
    restaurant_pizza4 = Restaurant_pizza(restaurant_id=restaurant2.id, pizza_id=pizza3.id)
    db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3, restaurant_pizza4])
    db.session.commit()

print("Seed completed.")
