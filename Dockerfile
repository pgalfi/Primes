FROM python:3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /Primes

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

RUN python manage.py test primenumbers

CMD python manage.py runserver 0.0.0.0:80
