import socket
import threading

HOST = '127.0.0.1'
PORTA = 8000

def receber_mensagens(conexao):
    while True:
        try:
            mensagem = conexao.recv(1024).decode('utf-8')
            if not mensagem:
                break
            print(f"\n{mensagem}")
        except:
            break

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORTA))

    threading.Thread(target=receber_mensagens, args=(cliente,), daemon=True).start()

    print("[+] Conectado ao chat. Digite mensagens (ou 'sair' para encerrar).")
    while True:
        mensagem = input()
        if mensagem.strip().lower() == "sair":
            break
        cliente.send(mensagem.encode('utf-8'))

    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()
