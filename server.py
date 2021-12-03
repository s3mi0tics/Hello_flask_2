from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/say/<name>')
def hi(name):
    print(name)
    return "Hi " + name + "!"

@app.route('/repeat/<int:number>/<name>')
def repeat_n_times(number, name):
    print(number, name)
    return name * number

# @app.route('/<anything_else>')
# def sorry():
#     return "Sorry, no response. Try again!"

if __name__=="__main__":
    app.run(debug=True)

