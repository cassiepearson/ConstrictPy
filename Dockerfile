FROM ubuntu:16.04

RUN adduser serveruser

WORKDIR /home/serveruser

ARG CRAN_MIRROR=https://cran.revolutionanalytics.com/
RUN apt-get update && \
  apt-get install -y \
  apt-utils \
  apt-transport-https \
  dirmngr \
  gnupg \
  libcurl4-openssl-dev \
  libnlopt-dev \
  lsb-release && \
  echo "deb ${CRAN_MIRROR}/bin/linux/ubuntu $(lsb_release -c -s)/" \
       >> /etc/apt/sources.list.d/added_repos.list && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
  apt-get update -qq && \
  apt-get install -y \
  python3 python3-pip python3-venv \
  r-base r-base-dev

COPY requirements.txt requirements.txt
COPY app app
COPY constrictpy constrictpy
COPY ConstrictR ConstrictR
COPY logs logs
COPY setup.py webapp.py config.py boot.sh ./

RUN \
  python3 -m pip --no-cache-dir install pip --upgrade && \
  python3 -m pip --no-cache-dir install setuptools --upgrade && \
  python3 -m pip --no-cache-dir install wheel --upgrade && \
  python3 -m pip --no-cache-dir install -r requirements.txt && \
  rm -rf /root/.cache

RUN python3 -m pip install .
RUN chmod +x boot.sh

ENV FLASK_APP webapp.py

RUN chown -R serveruser:serveruser ./
USER serveruser

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
