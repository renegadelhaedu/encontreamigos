from flask import *
import dao

app = Flask(__name__)
app.secret_key = 'ASsadlkjasdAJS54$5sdSA21'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def verificarlogin():
    if request.method == 'GET':
        return render_template('pagelogin.html')
    elif request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        result = dao.verificarlogin(email, senha)
        if len(result) > 0:
            session['email'] = email
            path = result[0][3]

            return render_template('home.html', email=email, foto=path)

        else:
            texto='login ou senha incorretos'
            return render_template('index.html', msg=texto)



@app.route('/cadastrarusuario', methods=['GET', 'POST'])
def cadastrarUser():
    if request.method == 'GET':
        return render_template('cadastraruser.html')
    elif request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        f = request.files['file']
        path = 'static/imagens/' + f.filename

        if dao.inseriruser(email, nome, senha, path):
            f.save(path)
            texto = 'Usuário cadastrado com sucesso'
            return render_template('index.html', msg=texto)
        else:
            texto = 'Usuário já cadastrado. Tente novamente'
            return render_template('index.html', msg=texto)

@app.route('/logout')
def logout():
    #removeu do servidor
    session.pop('email', None)

    res = make_response("Cookie Removido")
    res.set_cookie('email', '', max_age=0)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)