from flask import Blueprint, render_template
main = Blueprint("main", __name__)

@main.route("/<username>")
def register(username):
    return render_template("register.html")


@main.route("/profile/<username>")
def login(username):
    return render_template("login.html", username=username)

@main.route("/accounts")
def logout():
    return render_template("logout.html")


@main.route("/me/<username>")
def profile(username):
    return render_template("profile.html", username=username)

@main.route("/verify/<username>")
def verify(username):
    return render_template("verify.html", username=username)   

@main.route("/settings/<username>")
def settings(username):
    return render_template("settings.html", username=username)  

@main.route("/dashboard/<username>")
def dashboard(username):
    return render_template("dashboard.html", username=username)

@main.route("/dashboard/<username>")
def dashboard(username):
    return render_template("dashboard.html", username=username)

@main.route("/dashboard/<username>")
def dashboard(username):
    return render_template("dashboard.html", username=username)
