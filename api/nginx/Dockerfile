# syntax=docker/dockerfile:1

FROM nginx:stable-perl

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80 443