from flask import Flask, jsonify
from base.scraper import *

# from flask_restful import Api, Resource, reqparse
# from api.TravelApiHandler import TravelApiHandler

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
# api = Api(app)


# POST /user data: {tripName:}
@app.route('/trip_plan', methods=["POST"])
def create_plan():
    pass


# GET /attractions/<string:city>
@app.route('/attractions/<string:city_name>', methods=['GET'])
def get_attractions(city_name):
    attractions = find_attractions(city_name, 1)
    return json.dumps(get_all_attraction_data(city_name, attractions), indent=4)

# GET /Best planned Attractions
@app.route('/attractions')
def get_attractions_near():
    response_body = {
        "name": "Nagato",
        "about":"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body


@app.route('/attractions/<string:city_name>/place')
def get_attractions_place(name):
    pass


@app.route('/')
def serve():  # put application's code here
    return '<h1>Welcome To Wanderlag!</h1>'


# api.add_resource(TravelApiHandler, '/flask/content')

if __name__ == '__main__':
    app.run()
