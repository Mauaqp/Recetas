from flask_app import app
from flask_app.controllers import c_users, c_recipes


if __name__ == "__main__":
    app.run( debug = True )