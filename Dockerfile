FROM python:2
COPY requirements.txt /requirements.txt
COPY simple.py /simple.py
COPY flask_start.sh /flask_start.sh
