from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def one():
    return "Hello World!"

@app.route('/dojo')
def two():
    return "Dojo!"

@app.route('/say/<string:word>')
def three(word):
    return "Hi " + word.capitalize() + "!"

@app.route('/repeat/<int:num>/<string:word>')
def four(num, word):
    return (word + " ") * num

if __name__=="__main__":
    app.run(debug=True)