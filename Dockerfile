FROM python:3.9

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY setup.py README.rst requirements.txt /usr/src/app/
COPY random_joke_generator/ /usr/src/app/random_joke_generator
RUN pip install -r requirements.txt
RUN python setup.py install

EXPOSE 9600

CMD python random_joke_generator