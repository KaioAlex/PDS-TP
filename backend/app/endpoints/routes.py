# from flask import Flask, render_template, request, redirect, url_for, Response


# app = Flask(__name__)

# # Lista de tarefas (inicialmente vazia)
# tasks = []

# @app.route('/')
# def index():
#     return render_template('index.html', tasks=tasks)

# @app.route('/add_task', methods=['POST'])
# def add_task():
#     task = request.form.get('task')
#     tasks.append(task)
#     return redirect(url_for('index'))

# @app.route('/edit_task/<int:index>', methods=['GET', 'POST'])
# def edit_task(index):
#     if request.method == 'POST':
#         updated_task = request.form.get('updated_task')
#         tasks[index] = updated_task
#         return redirect(url_for('index'))
#     return render_template('edit_task.html', task=tasks[index])

# @app.route('/delete_task/<int:index>')
# def delete_task(index):
#     del tasks[index]
#     return redirect(url_for('index'))


# @app.route('/teste', methods=['POST'])
# def teste():
#     print("sua mae é minha aquela vagabunda\n\n\n")
#     return Response(status=200)


from flask import render_template, request, redirect, url_for, Response
from app import app

# Lista de tarefas (exemplo)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Adicione outras rotas aqui...

@app.route('/teste', methods=['POST'])
def teste():
    print("Sua mensagem aqui...\n\n\n")
    return "Resposta do teste"

@app.route('/teste2', methods=['POST'])
def teste2():
    print("sua mae é minha aquelas vagabunda\n\n\n")
    return Response("deu certo",status=200)