from flask import Blueprint, render_template, abort
main = Blueprint("main", __name__)

@main.route("/<username>")
def profile(username):
    if username == "admin":
        return render_template("admin.html")
    else:
        abort(404)
