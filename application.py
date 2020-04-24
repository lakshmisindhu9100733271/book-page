import os

from flask import Flask, session,render_template,request,session,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from registerdb import db,Users


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "username"
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        user = request.form.get("name")
        if user == "Admin":
            message = "Dear Admin please login"
            return render_template("login.html",message=message)
        else:
            return redirect(url_for("register"))

    return render_template("index.html")

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        gender = request.form.get("name")
        new_user=Users(username = username, password = password, email = email, gender = gender)
        try:
            db.session.add(new_user)
            db.session.commit()
            print(username, password, email, gender)
            message = "successfully registered"
            return render_template("success.html",message = message)
        except:
            msg = "sorry your credentials are wrong. please try again"
            return render_template("registration.html",message = msg)
    msg = "Please fill in this form to create an account."
    return render_template("registration.html",message = msg)

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "janu@janu" and password == "Rk@123456":
            session["Admin"] = username
            return redirect(url_for("admin"))
        user = Users.query.get(username)
        if user != None:
            if password == user.password:
                session["email"] = username
                return redirect(url_for("home"))
            else:
                message = "Wrong Password please try again"
                return render_template("login.html",message=message)
        return render_template("success.html")
    return render_template("login.html")

@app.route("/admin")
def admin():
    if session["Admin"] is None:
        return redirect(url_for("register"))
    data = Users.query.order_by(Users.time.desc()).all()
    return render_template("admin.html",data=data)
@app.route("/home")
def home():
    if session["email"] is None:
        return redirect(url_for("register"))
    message = session["email"]
    return render_template("homepage.html",username=message)

@app.route("/logout")
def logout():
    if not session["Admin"] is None:
        session["Admin"] = None
    session["email"] = None
    message = "You have sucessfully logged out"
    return redirect(url_for("register"))