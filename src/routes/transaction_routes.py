from flask import Blueprint, render_template, abort
main = Blueprint("main", __name__)

@main.route("/register")
def register():
    return render_template("register.html")

