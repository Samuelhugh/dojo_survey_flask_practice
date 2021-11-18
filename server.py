from flask_app.controllers import dojos
from env import key


from flask_app import app
app.secret_key = key


if __name__ == '__main__':
    app.run(debug=True)