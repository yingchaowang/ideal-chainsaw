
from flask import Flask, make_response, request
app = Flask(__name__)

@app.route("/")
def simple():
    return "<h1>Flask Index Page</h1>"

@app.route("/newview")
def simple():
    return "<h1>Your New View</h1>"

@app.route("/add_routes")
def new_route():
    return "<h1>added more routes</h1>"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route("/getme")
def get_route():
    myval = request.args.get('arg', 'empty')
    try:
        myval = int(myval)
    except ValueError as e:
        pass
    try:
        myval = float(myval)
    except ValueError as e:
        pass
    if isinstance(myval, str) or isinstance(myval, unicode):
        myval = "I'm a string! " + myval
    elif isinstance(myval, int):
        myval = "I'm an integer! " + str(myval + 20)
    elif isinstance(myval, float):
        myval = "I'm a float! " + str(myval + 20.05)
    else:
        myval = "I'm not a str or an int! \_(o_O)_/ I'm a '%s' and myval is %s" % (type(myval), str(myval))
        
    return "<h1>%s</h1>" % myval
    ## TODO set est based on args
    #est = estimators.get(request.args.get('estimator', 'k_means_iris_3'))
    #ground_truth = request.args.get('ground_truth', False)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
