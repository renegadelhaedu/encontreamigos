import psycopg2

def conectar_render():
    conexao = psycopg2.connect(
        host='dpg-cnqu148l5elc73avqjlg-a.oregon-postgres.render.com',
        database='ferascompcloud',
        user='ferascompcloud_user',
        password='6ErVy4FPtb9T9w5gjcpJN73gbdsbN2KI'

    )
    return conexao


def listar_usuarios():
    conexao = conectar_render()
    cursor = conexao.cursor()
    sql = 'select * from usuarios'
    cursor.execute(sql)

    results = cursor.fetchall()
    print(results)

def login(usuario, senha):
    conexao = conectar_render()
    cursor = conexao.cursor()
    sql = f"select * from usuarios where email='{usuario}' and senha='{senha}' "
    cursor.execute(sql)

    results = cursor.fetchall()
    print(results)
    if(len(results) > 0):
        if(results[0][2] == 'adm'):
            return 1
        else:
            return 2
    else:
        return 0

saida = login('teste@teste', '123')

if(saida == 1):
    print('renderizar page do ADM')
elif(saida == 2):
    print('renderizar page do cliente')
else:
    print('renderizar page de index com mensagem de erro no login')


