from flask import (
                render_template,
                request)
from werkzeug.wrappers import Response
from core.forms.registration import RegistrationForm
from core.forms.login import LoginForm
from core.models.users import Users
from core.models.posts import Posts
from utils import login_required
from forms.post import NewPostForm


def configure_routes(app):

    @app.errorhandler(404)
    def page_not_found(error) -> Response:
        """
        only thing certain in life is error 404  ;)
        :return: return template with error
        """
        return render_template('404.html', error=404)

    @app.route('/')
    def home() -> Response:
        """
        rendering main  page
        """
        return render_template('main.html')

    @app.route('/posts/list/')
    def posts_list():
        """ render list of all posts """
        posts = Posts().get_all_posts()
        return render_template('list.html', posts=posts)

    @app.route('/posts/<string:tag>')
    def posts_by_tag(tag):
        """ render list of posts filtered by tags/category"""
        posts_by_tags = Posts.get_posts_by_tag(tag)
        return render_template('post.html', posts=posts_by_tags, tag=tag)

    @app.route('/create-new-post/', methods=['POST', 'GET'])
    def create_post() -> Response:
        """
        create  new post by registered user
        """
        form = NewPostForm(request.form)
        if form.validate_on_submit():
            Posts().create_post()

        return render_template('new_post.html', form=form)

    @app.route('/update-post/<string:post_id>', methods=['PUT', 'PATCH'])
    def update_post(post_id) -> Response:
        """
        update post detail
        :return: in progress
        need to improve update function
        """
        post = Posts().get_post(post_id)
        form = NewPostForm(request.form)
        if form.validate_on_submit():
            Posts().update_post(id)

        return render_template('update_post.html', post=post)

    @app.route('/delete-post/<string:post_id>', methods=['DELETE'])
    def delete_post(post_id) -> Response:
        """
        delete choosen by user post
        :return:
        """
        return Posts().delete_post(post_id)

    @app.route('/user/registered', methods=['POST', 'GET'])
    def register_user() -> Response:
        """
        render user registration form
        :return: registered user, if registration  failed - render registration form view
        """
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate():
            return Users().signup()
        return render_template('registration.html', form=form)


    @app.route('/user/signout/', methods=['GET', 'POST'])
    def signout() -> Response:
        """ signout/logout user, ending user session"""
        return Users().signout()

    @app.route('/user/login', methods=['POST', 'GET'])
    def login():
        """ login  users and starts user session"""
        form = LoginForm(request.form)
        if form.validate_on_submit():
            return Users().login()

        return render_template('login.html', form=form)

    @app.route('/dashboard/', methods=['POST', 'GET'])
    @login_required
    def generate_dashboard() -> Response:
        """
        generate user profile/dashboard with user details, need to add possibility to save fav posts
        """
        return render_template('navigation.html')
