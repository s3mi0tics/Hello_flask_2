from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/say/<string:name>')
def hi(name):
    print(name)
    return "Hi " + name.capitalize + "!"

@app.route('/repeat/<int:number>/<string:word>')
def repeat_n_times(number, word):
    output = ''

    for i in range (0,number):
        output += f'<p>{word}<p>'
    print(number, word)
    return output

# @app.route('/<anything_else>')
# def sorry():
#     return "Sorry, no response. Try again!"

if __name__=="__main__":
    app.run(debug=True)

