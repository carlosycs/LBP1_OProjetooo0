from flask import Flask, render_template
from controllers.blueprint import *


app = Flask(__name__)
app.register_blueprint(validar)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)