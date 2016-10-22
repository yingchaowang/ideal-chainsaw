FROM jenkins

USER root
RUN apt-get update \
      && apt-get install -y sudo python-dev python-pip
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

USER jenkins

