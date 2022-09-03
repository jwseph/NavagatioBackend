from flask import Flask
from flask_restful import Resource, Api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] =     'sqlite:///'+os.path.join(basedir,'data.sqlite')
# app.config['SQLALCEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# Migrate(app, db)
api = Api(app)


class TopTrips(Resource):

    def get(self):
        return {"top_trips": ["Beijing", "Los Angeles", "Tokyo"]}


class ProcessedPlan(Resource):

    def post(self, city_name):
        search = {"searched":city_name}
        return search

# Top Trips (Returning most popular trips near you)
api.add_resource(TopTrips, '/trips')
# Returns PROCESSED TRIP PLAN (AI Data)
api.add_resource(ProcessedPlan, '/plans/<string:city_name>')

# POST /user data: {tripName:}
@app.route('/trip_plan', methods=["POST"])
def create_plan():
    pass


# GET /attractions/<string:city>
@app.route('/plans/<string:city_name>', methods=['GET'])
def get_attractions(city_name):
    pass


@app.route('/attractions/<string:city_name>/place')
def get_attractions_place(name):
    pass

if __name__ == '__main__':
    app.run(debug=True)
