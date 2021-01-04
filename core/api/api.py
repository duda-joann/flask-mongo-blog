from app import app
from flask_restful import Api, Resource

api = Api(app)


class PostsAllApi(Resource):
    def get(self, id):
        pass

    def post(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass




api.add_resource(PostsAllApi, '/api/v1/posts/<int:posts>' )






