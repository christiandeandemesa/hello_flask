from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def standard():
    return render_template("checkerboard.html", row=8, col=8, color1='gold', color2='rebeccapurple')

@app.route('/<int:x>')
def row(x):
    return render_template("checkerboard.html", row=x, col=8, color1='gold', color2='rebeccapurple')

@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template("checkerboard.html", row=x, col=y, color1='gold', color2='rebeccapurple')

@app.route('/<int:x>/<int:y>/<string:color1>')
def row_col_color_one(x, y, color1):
    return render_template("checkerboard.html", row=x, col=y, color1=color1, color2='rebeccapurple')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def row_col_color_two(x, y, color1, color2):
    return render_template("checkerboard.html", row=x, col=y, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)