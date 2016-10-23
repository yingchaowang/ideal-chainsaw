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
    res = conn.execute ('select * from users')
    for r in res:
      html +='<br/>' + str(r)
    return html

@app.route('/useradd/<username>')
def add_users(username):
    html = '<h1>adding: %s</h1>' % username
    try:
        conn.execute('INSERT INTO users VALUES (\'%s\', FALSE, FALSE)' % username)
        res ='<h2>success</h2>'
    except Exception as e:
        res ='<h2>faliure: ' + e.message + '</h2>'
    return html + res

@app.route('/userdel/<username>')
def del_user(username):
    html = '<h1>deleting: %s</h1>' % username
    try:
        r=conn.execute('DELETE FROM users WHERE email = \'%s\'' % username)
        if r.rowcount == 0:
            raise ValueError('user %s was not deleted' % username)
        res = '<h2>success</h2>'
    except Exception as e:
        res = '<h2>failure: ' + e.message + '</h2>'
    return html + res

if __name__ == "__main__":
    app.run(host='0.0.0.0')
