from flask import Blueprint, render_template, request

validar = Blueprint('cachorro', __name__)

@validar.route("/login", methods=['POST'])
def index():
        user = request.form['user']
        senha = request.form['senha']
        return render_template('login.html')


