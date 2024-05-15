import threading
import time
def atualizarlistaProdutos(opcao):

    if opcao == 1:
        print('1')
    else:
        print('2')
    print('vai comecar')
    time.sleep(20)
    print('terminou')

def atualizar_user():
    print('vai demorar agora')
    time.sleep(22)

def atualizarComThread(opcao):
    threading.Thread(target=atualizarlistaProdutos, args=(opcao,)).start()

