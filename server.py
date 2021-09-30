from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/say/<string:name>')
def hi(name):
    return f"Hi, {name.capitalize()}"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    string = ""
    for i in range(0, num):
        string += f"{word}\n"
    return string

if __name__=="__main__":
    app.run(debug=True)