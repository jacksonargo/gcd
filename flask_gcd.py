from gcd import gcd
from flask import Flask

app = Flask(__name__)

@app.route('/gcd')
def flask_gcd_help():
    return "Operations:\n\t/gcd/n1/n2\tReturns the GCD of n1 and n2."

@app.route('/gcd/<int:n1>/<int:n2>')
def flask_gcd(n1, n2):
    return gcd(n1, n2)
