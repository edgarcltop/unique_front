from flask import Blueprint, render_template, abort
main = Blueprint("main", __name__)

@main.route("/register")
def register():
    return render_template("register.html")


@main.route("/login")
def login():
    return render_template("login.html")

@main.route("/logout")
def logout():
    return render_template("logout.html")

@main.route("/me")
def profile():
    return render_template("profile.html")

@main.route("/verify")
def verify():
    return render_template("verify.html")

@main.route("/verify")
def verify(username):
    return render_template("verify.html", username=username)
