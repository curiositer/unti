from flask import Flask

app = Flask(__name__)   # __name__为模块名


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

