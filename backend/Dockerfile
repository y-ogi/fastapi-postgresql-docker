FROM python:3.9.15-bullseye
USER root

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

RUN mkdir -p /root/app
COPY requirements.txt /root
WORKDIR /root

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt