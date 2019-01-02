 FROM python:3.6

 ENV PYTHONUNBUFFERED 1
 
 RUN mkdir /app
 WORKDIR /app
  
 RUN pip install pipenv

 ADD Pipfile /app/
 ADD Pipfile.lock /app/
 
 RUN pipenv install

 ADD . /app/