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
        print(f'Mensagem de {peer_name}: {data.decode('utf-8')}')
        
        if not data:
            connection.sendall(data)

        # print(f'Mensagem recebida: {data.decode('utf-8')}')

        

        message = input('Digite uma mensagem: ')


        connection.sendall(message.encode('utf-8')) #formata o dado e codifica antes de enviar

    connection.close()
    s.close()

def client(name):

    server_address = ('127.0.0.1', 5000) #define host e porta usados
    message = ''

    #familia INET é IPv4 e SOCK_STREAM é o tipo de socket TCP
    novo_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criou objeto de socket
    novo_socket.connect(server_address) #inicia conexão com servidor TCP
    print(f'Olá, {name}!')
    novo_socket.sendall(name.encode('utf-8'))
    data = novo_socket.recv(1024)
    peer_name = data.decode('utf-8')
    while message != 'fim':
        message = input('Digite uma mensagem: ')
        novo_socket.sendall(message.encode('utf-8'))#formata mensagem em str e depois codifica e envia
        #sendall garante que todos os bytes enviados serão transmitidos

        #AGUARDA RESPOSTA DO SERVIDOR

        data = novo_socket.recv(1024) #recebe mensagem usando TCP, 1024 tamanho do buffer
        print(f'Mensagem de {peer_name}: {data.decode('utf-8')}') #exibe mensagem recebida

    novo_socket.close() #encerra canal de comunicação

def main(peer_type, user_name):
    if peer_type == 'servidor':
        server(user_name)
    
    if peer_type == 'cliente':
        client(user_name)

if __name__=='__main__':
    peer_type = sys.argv[1]
    user_name = sys.argv[2]

    main(peer_type, user_name)