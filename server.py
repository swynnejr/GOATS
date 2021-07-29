from flask_app import app

from flask_app.controllers import goats, login, athletes

if __name__ == "__main__":
    app.run (debug = True)