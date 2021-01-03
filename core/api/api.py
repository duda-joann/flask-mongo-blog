from app import app
from flask_restful import Api, Resource

api = Api(app)


class PostsAllApi(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
