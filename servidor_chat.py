import socket
import threading

HOST = '127.0.0.1'
PORTA = 8000

clientes = []

def tratar_cliente(conexao, endereco):
    print(f"[+] Cliente conectado: {endereco}")
    while True:
        try:
            mensagem = conexao.recv(1024).decode('utf-8')
            if not mensagem:
                break
            print(f"{endereco}: {mensagem}")
            for c in clientes:
                if c != conexao:
                    c.send(f"{endereco[0]}:{endereco[1]}: {mensagem}".encode('utf-8'))
        except:
            break
    clientes.remove(conexao)
    conexao.close()
    print(f"[-] Cliente desconectado: {endereco}")

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORTA))
    servidor.listen()
    print(f"[*] Servidor de Chat rodando em {HOST}:{PORTA}...")

    while True:
        conexao, endereco = servidor.accept()
        clientes.append(conexao)
        threading.Thread(target=tratar_cliente, args=(conexao, endereco), daemon=True).start()

if __name__ == "__main__":
    iniciar_servidor()
