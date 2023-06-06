FROM ubuntu:latest

RUN apt update
RUN apt -y full-upgrade

RUN apt -y install python3 python3-pip

COPY . /opt/app
WORKDIR /opt/app

RUN pip3 install -r requirements.txt 
