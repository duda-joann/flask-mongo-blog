from flask import Flask, render_template, session, request
from core.forms.registration import RegistrationForm
from core.forms.login import LoginForm
from core.models.users import Users
from core.common.db import mongo
from utils import login_required

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'blog'
app.config['MONGO_URI'] = "mongodb+srv://root:root1234@cluster0.qabhw.mongodb.net/<dbname?retryWrites=true&w=majority"
SECRET_KEY = 'nojeszczeczego?!?!'
app.config['SECRET_KEY'] = SECRET_KEY
mongo.init_app(app)


@app.route('/')
def main_view():
    posts = mongo.db.Posts.find({})
    return render_template('main.html', posts = posts)


@app.route('/user/signup/', methods=['POST', 'GET'])
def signup():
    form = RegistrationForm(request.form)
    return render_template('registration.html', form=form)


@app.route('/user/registered', methods=['POST'])
def register_user():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        return Users().signup()
    return render_template('login.html', email=session['email'])


@app.route('/user/signout/')
def signout():
    return Users().signout()


@app.route('/user/login', methods = ['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        return Users().login()

    return render_template('login.html', form=form)


@app.route('/dashboard/')
@login_required
def generate_dashboard():
    return render_template('navigation.html')


if __name__ == "__main__":
    app.run(debug=True)



