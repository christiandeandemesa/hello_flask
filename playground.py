from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def level_one():
    return render_template('playground.html', num = 3, color = 'lightblue')

@app.route('/play/<int:x>')
def level_two(x):
    return render_template('playground.html', num = x, color = 'lightblue')

@app.route('/play/<int:x>/<string:color>')
def level_three(x, color):
    return render_template('playground.html', num = x, color = color)

if __name__=="__main__":
    app.run(debug=True)