import sqlalchemy

from flask import Flask, make_response, request, render_template
app = Flask(__name__)

conn_string = 'postgres://flask:secret@db:5432/flask'
conn = sqlalchemy.create_engine(conn_string, client_encoding='utf8')

@app.route("/")
def simple():
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

if __name__ == "__main__":
    app.run(host='0.0.0.0')
