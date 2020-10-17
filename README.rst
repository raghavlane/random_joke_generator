random_joke_generator
=====================

A web server which returns a random joke with a random name.

Usage
'''''
To install the app 
::
    python3 setup.py install

To run the app 
::
    python3 random_joke_generator

Testing
'''''''
::

    python3 -m unittest 
or 
::

    python3 setup.py test


Docker build
'''''''
::

    docker build -t <imagename>  .

Running docker image
'''''''
::
    docker run -p 9600:9600 <imagename> 
    