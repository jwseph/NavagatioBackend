from flask_restful import Api, Resource, reqparse

class TravelApiHandler(Resource):
    def get(self):
        return {
            'resultStatus':'SUCCESS',
            'message':'Travel Api Handler'
        }

    