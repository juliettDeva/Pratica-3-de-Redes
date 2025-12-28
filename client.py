import socket #acesso as funções deste módulo

server_address = ('127.0.0.1', 5000) #define host e porta usados
message = ''

#familia INET é IPv4 e SOCK_STREAM é o tipo de socket TCP
novo_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criou objeto de socket
novo_socket.connect(server_address) #inicia conexão com servidor TCP

while message != 'fim':
    message = input('Digite uma mensagem: ')
    novo_socket.sendall(message.encode('utf-8'))#formata mensagem em str e depois codifica e envia
    #sendall garante que todos os bytes enviados serão transmitidos

    #AGUARDA RESPOSTA DO SERVIDOR

    data = novo_socket.recv(1024) #recebe mensagem usando TCP, 1024 tamanho do buffer
    print(f'Recebendo a mensagem do servidor: {data.decode('utf-8')}') #exibe mensagem recebida

novo_socket.close() #encerra canal de comunicação

