from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    first_name = request.args.get('first_name')
    return render_template('index.html', first_name=first_name)


@app.route('/contact')
def contact():
    return render_template('contact.html')


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
