

FROM python:3


ENV PYTHONUNBUFFERED 1


WORKDIR /app

COPY . .



RUN pip3 install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py test tracks




# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]




# Commands

# sudo docker build --tag track-test .
# sudo docker run -p 8000:8000 track-test

