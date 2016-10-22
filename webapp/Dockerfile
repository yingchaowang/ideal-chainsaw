FROM ubuntu
EXPOSE 80

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y python-pip python-dev python-psycopg2 nginx

COPY requirements.txt /requirements.txt
RUN  pip install -r /requirements.txt

COPY nginx.conf /etc/nginx/sites-available/default

COPY . /app
WORKDIR /app

CMD sh docker_start.sh
