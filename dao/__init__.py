import psycopg2

def conectardb():
    con = psycopg2.connect(
        host='localhost',
        database='encontreamigos',
        user='postgres',
        password='12345'
    )

    return con
def verificarlogin(email, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT * FROM usuarios WHERE email = '{email}' AND senha = '{senha}'")
    recset = cur.fetchall()
    conexao.close()

    return recset


def inseriruser(email, nome, senha, path):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuarios (email, nome, senha, pathft) VALUES ('{email}', '{nome}', '{senha}', '{path}' )"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito