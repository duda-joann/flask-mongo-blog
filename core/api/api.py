from core.run import app
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow
from models.posts import (Posts,
                          post_schema,
                          posts_schema)

ma = Marshmallow(app)
api = Api(app)


class GetAllPosts(Resource):
    @staticmethod
    def get():
        post = Posts().get_all_posts()
        return posts_schema.dump(post)


class GetSinglePostApi(Resource):
    def get(self, post_id: int):
        post = Posts().get_post(post_id)
        return post_schema.dump(post)

    def patch(self, post_id: int):
        post = Posts().update_post(post_id)
        return post_schema.dump(post)

    def post(self):
        post = Posts().create_post()
        return post_schema.dump(post)

    def delete(self, post_id: int):
        post = Posts().delete_post(post_id)
        return post_schema(post)


api.add_resource(GetSinglePostApi)


api.add_resource(GetAllPosts, '/api/v1/posts/')
api.add_resource(GetSinglePostApi, '/api/v1/posts/<int:post_id>')





