FROM python:3.8-alpine

RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip install Flask

ENV FLASK_APP=projet.py
ENV FLASK_ENV=development

COPY  . .

EXPOSE 5000
CMD [ "flask","run" ]
