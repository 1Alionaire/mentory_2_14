from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, HTTPS world!'

if __name__ == '__main__':
    app.run(debug=True, ssl_context=('server.crt', 'server.key'))


