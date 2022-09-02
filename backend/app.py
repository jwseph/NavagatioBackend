from flask import Flask, jsonify
import json
from api import api_utils

app = Flask(__name__, static_url_path='', static_folder='frontend/build')


# POST /user data: {tripName:}
@app.route('/trip_plan', methods=["POST"])
def create_plan():
    pass


# GET /attractions/<string:city>
@app.route('/attractions/<string:city_name>', methods=['GET'])
def get_attractions(city_name):
    return json.dumps(api_utils.get_all_attraction_data(city_name), indent=4)


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



if __name__ == '__main__':
    app.run()
