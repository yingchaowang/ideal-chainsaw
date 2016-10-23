About: Getting Flask to show me interesting matplot pngs

## By their powers *combine*!
https://gist.github.com/wilsaj/862153
http://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html#example-cluster-plot-mini-batch-kmeans-py

## Install some stuff

```bash
sudo pacman -S tk
sudo pip2 install scipy sklearn flask matplotlib
```

## Do things

```bash
python2 app.py

mkdir ~/ipython
docker run -d -p 127.0.0.1:8888:8888 -v $HOME/ipython:/home/jovyan/work -e NB_UID=$(id -u $USER) -e GRANT_SUDO=yes --user root  jupyter/datascience-notebook
Add Comment
```
`test
