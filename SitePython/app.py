from flask import Flask, render_template, request, flash
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Categorias
app.config['SECRET_KEY'] = '9ebe6f92407c97b3f989420e0e6bebcf9d1976b2e230acf9faf4783f5adffe1b'

# --> drive://usuario:senha@servidor/banco_de_dados

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/CategoriasGio"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aula')
@app.route('/aula/<nome>')
@app.route('/aula/<nome>/<curso>')
@app.route('/aula/<nome>/<curso>/<int:ano>')
def aula(nome = 'Gabriel', curso = 'Informática', ano = '1'):
    dados = {'nome':nome, 'curso':curso, 'ano':ano}
    return render_template('aula.html', dados_curso=dados)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/dados', methods=['POST'])
def dados():
    flash('Dados Enviados!!!')
    dados = request.form
    return render_template('dados.html', dados = dados)

@app.route("/categoria")
def categoriaprod():
    c = Categorias.query.all()
    return render_template("categoriaprod.html", dados = c)

if __name__ == '__main__':
    app.run()