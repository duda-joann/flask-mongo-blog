from app import app
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)
api = Api(app)


class GetSinglePostApi(Resource):
    def get(self, id):
        pass

    def post(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass




api.add_resource(GetSinglePostApi, '/api/v1/posts/<int:posts>' )






