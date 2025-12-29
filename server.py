import socket # acesso a funções de socket
import sys

def server(name):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criou objeto socket
    server_address = ('127.0.0.1', 5000) #socket precisa desta tupla
    s.bind(server_address) #socket vincula endpoint servidor e porta de socket
    s.listen(1) #espera algum cliente conectar

    print(f' Olá, {name}! Servidor aguardando conexão...')
    connection, address = s.accept() #aceita conexão

    message = ''
    data = connection.recv(1024)

    peer_name = data.decode('utf-8')
    connection.sendall(name.encode('utf-8'))
    while message != 'fim':
        data = connection.recv(1024) # método recv recebe mensagem TCP, 1024 é o tamanho do buffer
        print(f'Mensagem de {peer_name}: ', data.decode('utf-8'))
        
        if not data:
            connection.sendall(data)

        # print(f'Mensagem recebida: {data.decode('utf-8')}')

        

        message = input('Digite uma mensagem: ')


        connection.sendall(message.encode('utf-8')) #formata o dado e codifica antes de enviar

    connection.close()
    s.close()

if __name__ == '__main__':
    user_name = sys.argv[1]
    server(user_name)