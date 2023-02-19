from datetime import datetime, timedelta
from typing import Union

from . import app
from flask import render_template, redirect, url_for, Response
from .forms import LoginForm, SignUpForm
from .database import User, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .weather_api import get_weather, get_current_city
from .communicate_with_db import add_new_obj_to_db


@app.route('/')
@app.route('/main')
@login_required
def main() -> str:
    city = get_current_city()
    weather = get_weather()
    current_date = datetime.now()
    return render_template("main.html", weather=weather, date=current_date, timedelta=timedelta, city=city)


@app.route("/login", methods=('GET', 'POST'))
def login() -> Union[str, Response]:
    form = LoginForm()
    if form.validate_on_submit():
        user = session.query(User).where(User.nickname == form.nickname.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("main"))
    return render_template("login.html", form=form)


@app.route("/signup", methods=('GET', 'POST'))
def signup() -> Union[str, Response]:
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = User(
            nickname=form.nickname.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        add_new_obj_to_db(new_user)
        return redirect(url_for("login"))
    return render_template("signup.html", form=form)


@app.route('/logout')
def logout() -> Response:
    logout_user()
    return redirect(url_for("login"))


@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def handle_error(error):
    return render_template("error_page.html", code=error.code)
