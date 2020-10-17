"""This module serves as the entry point of random_joke_generator."""

import tornado.ioloop
import tornado.web
import requests
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        firstName , lastName = getRandomFirstLastName()
        if (firstName or lastName):
            joke = getRandomChuckNorrisJoke(firstName , lastName) 
            
            ''' 
            We can also replace the above  line with a different implementation as in the comments . But
            if the joke contains the string John or Doe , then the below string replace method will give unexpected result
            
            joke = getRandomChuckNorrisJoke()
            joke = joke.replace('John',firstName).replace('Doe',lastName)
            '''
            if joke:
                self.write(joke)
            else:
                self.write('Error while obtaining the joke')
        else:
            self.write('Error while obtaining name')


def getRandomFirstLastName():
    try:
        url = 'https://api.namefake.com'
        responseBody = getApiCall(url)
        if 'name' in responseBody:
            names = responseBody['name'].split(' ')
            return names[0],names[1]
    except Exception as e:
        print(e)
        return None , None

def getRandomChuckNorrisJoke( firstName = 'John' , lastName = 'Doe'):
    try:
        url = 'http://api.icndb.com/jokes/random?firstName={}&lastName={}&limitTo=[nerdy]'.format(firstName,lastName)
        responseBody = getApiCall(url)
        if (('value' in responseBody) and ('joke' in responseBody['value'])):
            return responseBody['value']['joke']
    except Exception as e :
        print(e)
        return None

def getApiCall(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.text) 
    except Exception as e:
        print(e)
        return None


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    port = 9600
    app = make_app()
    app.listen(port)
    print("Server started at port {}".format(port))
    tornado.ioloop.IOLoop.current().start()