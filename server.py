import socket # acesso a funções de socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criou objeto socket
server_address = ('127.0.0.1', 5000) #socket precisa desta tupla
s.bind(server_address) #socket vincula endpoint servidor e porta de socket
s.listen(1) #espera algum cliente conectar

print('Servidor aguardando conexão...')
connection, address = s.accept() #aceita conexão

message = ''

while message != 'fim':
    data = connection.recv(1024) # método recv recebe mensagem TCP, 1024 é o tamanho do buffer
    
    if not data:
        connection.sendall(data)

    print(f'Mensagem recebida: {data.decode('utf-8')}')

    

    message = input('Digite uma mensagem: ')


    connection.sendall(message.encode('utf-8')) #formata o dado e codifica antes de enviar

connection.close()
s.close()
