import sqlalchemy

from flask import Flask, make_response, request, render_template
app = Flask(__name__)

conn_string = 'postgres://flask:secret@db:5432/flask'
conn = sqlalchemy.create_engine(conn_string, client_encoding='utf8')

@app.route("/")
def simple():
    return render_template('index.html')

@app.route('/users')
def list_users():
    # show the user profile for that user
    html = '<h1>The Users</h1>'
    res = conn.execute ('selecr * from users')
    for r in res;
      html +='<br/>' + str(r)
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0')
