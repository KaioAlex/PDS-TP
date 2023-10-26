from flask import Blueprint, jsonify, Response, request, render_template
from flaskext.mysql import MySQL

mysql = MySQL()

def telas() -> Blueprint:
    telas_blueprint = Blueprint('telas', __name__)

    @telas_blueprint.route('/')
    def tela_inicial():
        return render_template('index.html')

    @telas_blueprint.route('/form')
    def tela_form():
        return render_template('form.html')

    @telas_blueprint.route('/login', methods = ['POST', 'GET'])
    def login():
        if request.method == 'GET':
            return "Login via the login Form"
     
        if request.method == 'POST':
            name = request.form['name']
            username = request.form['username']
            email = request.form['email']
            birth = request.form['birth']

            conn = mysql.connect()
            cursor = conn.cursor()

            # cursor.execute("SELECT * from users")
            # data = cursor.fetchall()
            # print(data)

            cursor.execute(''' INSERT INTO users (name, username, email, birth) VALUES(%s,%s,%s,%s)''',(name, username, email, birth))
            conn.commit()

            cursor.close()

            return f"Done!!"

    return telas_blueprint