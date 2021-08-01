from flask.helpers import url_for
from app.forms import LoginForm, RegistrationForm, SearchForm, UpdateForm
from app.models import Donor
from flask import render_template, redirect, flash, request
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = Donor(username=form.username.data, email=form.email.data,
                     password=hashed_password, contact=form.contact.data, state=form.state.data, city=form.city.data,
                     pincode=form.pincode.data, bloodgroup=form.bloodgroup.data, age=form.age.data, weight=form.weight.data,
                     gender=form.gender.data, lastdonation=form.lastdonation.data)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created!")
        return redirect(url_for('login'))
    return render_template('registration.html', title='Register', form=form)


#@app.route('/search', methods=['GET', 'POST'])
#def search():
 #   blood_group = request.args.get('bg')
  #  city = request.args.get('city')
   # return f'result for blood group {blood_group} and city {city}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('my_account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Donor.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('my_account'))
        else:
            flash('Login unsuccessful. Please check email and password')
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/my_account")
def my_account():
    return render_template('my_account.html', title="My Account")


@app.route("/update", methods=["GET", "POST"])
def update():
    form = UpdateForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.contact = form.contact.data
        current_user.state = form.state.data
        current_user.city = form.city.data
        current_user.pincode = form.pincode.data
        current_user.bloodgroup = form.bloodgroup.data
        current_user.age = form.age.data
        current_user.weight = form.weight.data
        current_user.gender = form.gender.data
        current_user.lastdonation = form.lastdonation.data
        db.session.commit()
        flash("Your account has been updated!")
        return redirect(url_for('my_account'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.contact.data = current_user.contact
        form.state.data = current_user.state
        form.city.data = current_user.city
        form.pincode.data = current_user.pincode
        form.bloodgroup.data = current_user.bloodgroup
        form.age.data = current_user.age
        form.weight.data = current_user.weight
        form.gender.data = current_user.gender
        form.lastdonation.data = current_user.lastdonation
    return render_template('update.html', title='Update Account', form=form)


@app.route("/cancel")
def cancel():
    return redirect(url_for('my_account'))


@app.route("/search", methods=["GET", "POST"])
def search():
    form=SearchForm()
    if form.validate_on_submit():
        city = form.city.data
        blood = form.blood.data
        results=Donor.query.filter_by(bloodgroup = blood , city=city).all()
        if not results:
            flash("No Results Available..")
        else:
            return render_template('result.html',results=results)
    return render_template('search.html',form=form)

