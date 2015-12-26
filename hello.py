from flask  import  Flask


#do not touch
app = Flask(__name__)

wsgi_app = app.wsgi_app
#end do not touch
#import all routes from route.py
from route import *;

#server lauching code

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_PORT','localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT','5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
