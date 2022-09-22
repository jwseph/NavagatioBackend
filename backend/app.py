from flask import Flask
from flask_restful import Resource, Api

from library.autocompleter import autocomp_init

app = Flask(__name__)

place_autocomplete = autocomp_init()
api = Api(app)


class TopTrips(Resource):

    def get(self):
        return {"results": ["Beijing", "Los Angeles", "Tokyo"]}


class ProcessedPlan(Resource):

    def post(self, city_name):
        search = {"searched":city_name}
        return search

class PlacesAutocomplete(Resource):

    def get(self, search_query):
        return {"results":place_autocomplete.autocomplete(search_query)}

# Top Trips (Returning most popular trips near you)
api.add_resource(TopTrips, '/search/')

# Returns PROCESSED TRIP PLAN (AI Data)
api.add_resource(ProcessedPlan, '/plans/<string:city_name>')

# Returns a list of possible results (up to 25)
api.add_resource(PlacesAutocomplete, '/search/<string:search_query>')


if __name__ == '__main__':
    app.run(debug=True)
