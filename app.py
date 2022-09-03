from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/saudacao')
def saudacao():
	return render_template('saudacao.html')


@app.route('/curso')
def curso():
	return render_template('cursos.html')


@app.route('/curso/<nome>')
def curso_por_nome(nome):
	if nome == 'devweb':
		return render_template('curso_devweb.html')
	elif nome == 'poo':
		return render_template('curso_poo.html')
	else:
		return "Curso inexistente"


@app.route('/curso/<nome>/<int:ano>')
def curso_com_dois_parametros(nome, ano):
	return "Rota de demonstração que recebe dois valores: nome={0} e ano={1}".format(nome, ano)


if __name__ == '__main__':
	app.run(debug=True)

