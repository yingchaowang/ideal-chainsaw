
from flask import Flask, make_response, request
app = Flask(__name__)

@app.route("/")
def simple():
    return "<h1>Flask Index Page</h1>"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

if __name__ == "__main__":
    app.run(host='0.0.0.0')
