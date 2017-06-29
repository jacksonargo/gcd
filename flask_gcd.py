from gcd import gcd
from flask import Flask

app = Flask(__name__)

@app.route('/gcd/<int:n1>/<int:n2>')
def flask_gcd(n1, n2):
    return gcd(n1, n2)
