import psycopg2
from psycopg2.extras import RealDictCursor

def conectardb():
    con = psycopg2.connect(
        #host='dpg-cog57pev3ddc73e6e3vg-a.oregon-postgres.render.com',
        #database='encontraramigos',
        #user='encontraramigos_user',
        #password='x2bd2iia6a62XKFE5gSGtIiY0is2oBCB'
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

def listarpessoas(opcao):
    conexao = conectardb()
    if opcao == 0:
        cur = conexao.cursor()
    else:
        cur = conexao.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"SELECT email,nome,pathft FROM usuarios")
    recset = cur.fetchall()
    conexao.close()

    return recset



def inserircurtida(admirador, crush):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO curtidas (admirador, crush) VALUES ('{admirador}', '{crush}')"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

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