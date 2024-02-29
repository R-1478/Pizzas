

You can run your Flask API on [`localhost:5555`](http://localhost:5555) by running:

```sh
python app.py
```

You can run your React app on [`localhost:4000`](http://localhost:4000) by running:

```sh
npm start --prefix client
```




## Models



- A `Restaurant` has many `Pizza`s through `RestaurantPizza`
- A `Pizza` has many `Restaurant`s through `RestaurantPizza`
- A `RestaurantPizza` belongs to a `Restaurant` and belongs to a `Pizza`


Add any code needed in the model files to establish the relationships.

Then, run the migrations and seed file:

```sh
flask db revision --autogenerate -m'message'
flask db upgrade
python db/seed.py
```




