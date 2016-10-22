FROM jenkins

USER root
RUN apt-get update \
      && apt-get install -y sudo python-dev python-pip python-psycopg2 libpq-dev
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

USER jenkins

