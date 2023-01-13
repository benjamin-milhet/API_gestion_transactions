FROM python:3.8-alpine


RUN pip install Flask

ENV FLASK_APP=projet.py
ENV FLASK_ENV=development

COPY  . .

EXPOSE 5000
CMD [ "flask","run" ]
