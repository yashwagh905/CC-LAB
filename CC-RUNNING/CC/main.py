from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<b>Hello, World!</b><br>CC Assignment Accomplished<br><b>Yash Wagh</b><br>12111124<br>AIDS-C-B3-74'


@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run()
