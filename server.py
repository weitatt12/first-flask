from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


# @app.route("/<name>")
# def index(name):
#     name = name.upper()
#     return render_template('index.html', name=name)


# @app.route("/another")
# def show():
#     return '<h1>Yo, Yo</h1>'

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
    # app.run(debug=True) #if there is error use this to see what is error
