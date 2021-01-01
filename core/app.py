from flask import (
                Flask,
                render_template,
                session,
                request)
from werkzeug.wrappers import Response
from core.forms.registration import RegistrationForm
from core.forms.login import LoginForm
from core.models.users import Users
from core.models.posts import Posts
from utils import login_required
from forms.post import NewPostForm
from core.common.db import db

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/blog"
SECRET_KEY = 'nojeszczeczego?!?!'
app.config['SECRET_KEY'] = SECRET_KEY
db.init_app(app)


@app.errorhandler(404)
def page_not_found(error) -> Response:
    """
    only thing certain in life is error 404  ;)
    :return: return template with error
    """
    return render_template('404.html', error = 404)

@app.route('/')
def main_view() -> Response:
    """
    rendering main  page
    """
    posts = Posts().get_all_posts()
    return render_template('main.html', posts = posts)


@app.route('/user/registered', methods=['POST', 'GET'])
def register_user() -> Response:
    """
    render user registration form
    :return: rregistered user, if registration  failed - render registration form view
    """
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        return Users().signup()
    return render_template('registration.html', email=session['email'])


@app.route('/user/signout/', methods=['GET', 'POST'])
def signout() -> Response:
    """ signout/logout user, ending user session"""
    return Users().signout()


@app.route('/user/login', methods = ['POST', 'GET'])
def login():
    """ login  users and starts user session"""
    form = LoginForm(request.form)
    if form.validate_on_submit():
        return Users().login()

    return render_template('login.html', form=form)


@app.route('/dashboard/', methods =['POST', 'GET'])
@login_required
def generate_dashboard() -> Response:
    """
    generate user profile/dashboard with user details, need to add possibility to save fav posts
    """
    return render_template('navigation.html')


@app.route('/create-new-post', methods = ['POST', 'GET'])
def create_post() -> Response:
    """
    create  new post by registered user
    """
    form = NewPostForm(request.form)
    if form.validate_on_submit():
        Posts().create_post()

    return render_template('new_post.html', form=form)


@app.route('/update-post/<string:post_id>', methods = ['POST', 'PUT'])
def update_post() -> Response:
    """
    update post detail
    :return: in progress
    need to improve update function
    """
    post = Posts().get_post(id)
    form = NewPostForm(request.form)
    if form.validate_on_submit():
        Posts().update_post(id)

    return render_template('update_post.html', post=post)


@app.route('/delete-post/<string:post_id>', methods = ['DELETE'])
def delete_post() -> Response:
    """
    delete choosen by user post
    :return:
    """
    return Posts().delete_post(id)


if __name__ == "__main__":
    app.run(debug=True)



