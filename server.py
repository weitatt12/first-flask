from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Why so hard?</h1>'


# @app.route("/another")
# def show():
#     return '<h1>Yo, Yo</h1>'

@app.route('/user/<username>')
def show(username):
    return f"Hi {username}"


if __name__ == '__main__':
    app.run()
