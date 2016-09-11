
from flask import Flask, make_response, request
app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return '''<h1>Flask Header</h1>
    <p><img src="/kmeans.png?estimator=k_means_iris_3" /><br/>kmeans 3 clusters</p>
    <p><img src="/kmeans.png?estimator=k_means_iris_8" /><br/>kmeans 8 clusters</p>
    <p><img src="/kmeans.png?estimator=k_means_iris_bad_init" /><br/>kmeans bad init</p>
    <p><img src="/kmeans.png?ground_truth=true" /><br/>ground truth'''

@app.route("/kmeans.png")
def simple():
    # imports from ipython
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    from sklearn.cluster import KMeans
    from sklearn import datasets

    # imports from flask plot example
    # https://gist.github.com/wilsaj/862153
    import datetime
    import StringIO
    import random

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    
    np.random.seed(5)
    
    centers = [[1, 1], [-1, -1], [1, -1]]
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    
    estimators = {'k_means_iris_3': KMeans(n_clusters=3),
                  'k_means_iris_8': KMeans(n_clusters=8),
                  'k_means_iris_bad_init': KMeans(n_clusters=3, n_init=1,
                                                  init='random')}
    # TODO set est based on args
    est = estimators.get(request.args.get('estimator', 'k_means_iris_3'))
    ground_truth = request.args.get('ground_truth', False)
    
    fig = plt.figure(figsize=(4, 3))
    plt.clf()
    ax = Axes3D(fig, rect=[0, 0, 0.95, 1], elev=48, azim=134)
    
    plt.cla()
    if not ground_truth:
        est.fit(X)
        labels = est.labels_
        ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=labels.astype(np.float))
    else:
        for name, label in [('Setosa', 0),
                            ('Versicolour', 1),
                            ('Virginica', 2)]:
            ax.text3D(X[y == label, 3].mean(),
                      X[y == label, 0].mean() + 1.5,
                      X[y == label, 2].mean(), name,
                      horizontalalignment='center',
                      bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
        # Reorder the labels to have colors matching the cluster results
        y = np.choose(y, [1, 2, 0]).astype(np.float)
        ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=y)
    
    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel('Petal width', labelpad=-10)
    ax.set_ylabel('Sepal length', labelpad=-10)
    ax.set_zlabel('Petal length', labelpad=-15)

    canvas=FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
