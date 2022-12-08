FROM node:lts-bullseye-slim
USER root

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

RUN mkdir -p /root/app
WORKDIR /root/app

RUN yarn global add @vue/cli @vue/cli-init