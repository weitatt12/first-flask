from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    signed_in = False
    return render_template('index.html', signed_in=signed_in)


@app.route('/contact')
def contact():
    signed_in = False
    return render_template('contact.html', signed_in=signed_in)


# @app.route("/<name>")
# def index(name):
#     name = name.upper()
#     return render_template('index.html', name=name)


# @app.route("/another")
# def show():
#     return '<h1>Yo, Yo</h1>'


if __name__ == '__main__':
    app.run()
    # app.run(debug=True) #if there is error use this to see what is error
