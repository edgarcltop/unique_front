from flask import Flask

Flask.__init__()


@app.route("/")
def init():
    return "Response"

@app.route("/register")
def register():
   return "gradient area"

