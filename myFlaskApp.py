from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return 'Hello, Everybody!'

@my_app.route('/foo')
def displayFoo():
    return 'testing foo'

@my_app.route("/A")
def displayA():
    return 'This should display A'

@my_app.route("/B")
def displayB():
    return 'This should display B'

if __name__ == '__main__':
   my_app.run()
