from flask import Blueprint, render_template, abort
main = Blueprint("main", __name__)

@main.route("/register")
def register():
    return render_template("register.html")

@main.route("/logout")
def logout():
    return render_template("logout.html")

@main.route("/verify-payment")
def verify_payment():
    return render_template("verify_payment.html")
