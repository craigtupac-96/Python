from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "This is the default webpage."


@app.route('/hello/<name>')
def hello(name="unkno"):
    return f"Hello {name} from my first webapp."


@app.route('/bye')
def bye():
    return "Bye bye from my first webapp."

if __name__ == '__main__':
    app.run(debug=True)

