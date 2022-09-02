from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='frontend/build')


# POST /user data: {tripName:}
@app.route('/trip_plan', methods=["POST"])
def create_plan():
    pass


# GET /attractions/<string:city>
@app.route('/plans/<string:city_name>', methods=['GET'])
def get_attractions(city_name):
    pass


# GET /Best planned Attractions
@app.route('/trips')
def get_top_trips():
    return {"top_trips": ["Beijing", "Los Angeles", "Tokyo"]}


@app.route('/attractions/<string:city_name>/place')
def get_attractions_place(name):
    pass


@app.route('/')
def serve():  # put application's code here
    return '<h1>Welcome To Wanderlag!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
