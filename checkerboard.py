from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def standard():
    return render_template('checkerboard.html', x=8, y=8, color1='black', color2='white')

@app.route('/4')
def half():
    return render_template('checkerboard.html', x=8, y=4, color1='black', color2='white')

@app.route('/<int:x>/<int:y>')
def multiple(x, y):
    return render_template('checkerboard.html', x=x, y=y, color1='black', color2='white')

@app.route('/<int:x>')
def row(x):
    return render_template('checkerboard.html', x=x, y=1, color1='black', color2='white')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def choose(x, y, color1, color2):
    return render_template('checkerboard.html', x=x, y=y, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)