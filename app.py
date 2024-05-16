from flask import *
import dao
import segundoplano as sp
from os.path import join, dirname, realpath


app = Flask(__name__)
app.secret_key = 'ASsadlkjasdAJS54$5sdSA21'
app.config['UPLOAD_FOLDER'] = 'static/imagens/'

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/atualizarprodutos')
def atualizarprods():
    sp.atualizarComThread('1')
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
        path = app.config['UPLOAD_FOLDER'] + f.filename

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

@app.route('/listarpessoas', methods=['GET'])
def listar_pessoas():
    if session.get('email') != None:
        result = dao.listarpessoas(0)
        return render_template('listarpessoas.html', pessoas=result, meuemail=session.get('email'))
    else:
        return 'nao ok'

@app.route('/buscarnome/<nome>')
def buscar_nome(nome):
    user = dao.buscar_pessoa(nome)
    print(user)
    return 'ok deu certo'

@app.route('/listarpessoas/externo', methods=['GET', 'POST'])
def listar_pessoas_ext():
    if(request.method == 'POST'):
        valor = request.json
        print(valor)
        result = dao.listarpessoas(1)
        return jsonify(result).json
    else:

        if session.get('email') != None:
            result = dao.listarpessoas(1)
            return jsonify(result).json
        else:
            resp = make_response('necessário fazer login')
            resp.status_code = 511
            return resp

@app.route('/listarpessoas/externoSemlogin', methods=['GET'])
def listar_pessoas_ext_semlogin():

    result = dao.listarpessoas(1)
    return jsonify(result).json

@app.route('/curtirpessoa', methods=['GET'])
def curtir_pessoa():
    if session.get('email') != None:
        email = request.values.get('user1')
        crush = request.values.get('user2')
        if dao.inserircurtida(email, crush):
            return 'deu certo'
        else:
            return 'deu errado'


@app.route('/atualizarbd')
def atualizar_bd():
    sp.atualizarComThread(1)
    return render_template('index.html')


@app.route('/exemplo')
def exemplo():
    if session.get('email') != None:
        return 'entrei no perfil de ' + session.get('email')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)