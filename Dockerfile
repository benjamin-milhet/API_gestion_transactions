FROM python:3.8-alpine

RUN apt-get update 
RUN apt-get install -y python3-pip
RUN pip install Flask

ENV FLASK_APP=main.py
ENV FLASK_ENV=development

COPY  . .

EXPOSE 5000
CMD [ "flask","run" ]
