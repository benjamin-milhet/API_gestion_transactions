FROM python:3.8-alpine
RUN pip install Flask

ENV FLASK_APP=main.py
ENV FLASK_ENV=development

EXPOSE 5000
CMD [ "flask","run" ]
