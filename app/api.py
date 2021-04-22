from flask_restplus import Api, Resource

api = Api()

@api.route('/users')
class User(Resource):
    def get(self):
        return {'user': 'name'}