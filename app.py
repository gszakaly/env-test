from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    s = '<html><body>'
    for name in os.environ:
        s += name + ': ' + os.environ[name] + '<br>'
    s += '</body></html>'

    return s

app.run(host='0.0.0.0')