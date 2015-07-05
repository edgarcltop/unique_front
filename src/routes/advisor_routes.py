from flask import Blueprint, render_template, abort
main = Blueprint("main", __name__)

@main.route("/advisor/<username>")
def advisor(username):
    return render_template("advisor.html", username=username)

@main.route("/advisor/settings/<username>")
def advisor_settings(username):
    return render_template("advisor_settings.html", username=username)


@main.route("/advisor/settings/<username>")
def advisor_settings(username):
    return render_template("advisor_settings.html", username=username)

@main.route("/advisor/settings/<username>")
def advisor_settings(username):
    return render_template("advisor_settings.html", username=username)

@main.route("/advisor/settings/<username>")
def advisor_settings(username):
    return render_template("advisor_settings.html", username=username)


@main.route("/advisor/settings/<username>")
def advisor_settings(username):
    return render_template("advisor_settings.html", username=username)