import socket # acesso a funções de socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criou objeto socket
server_address = ('127.0.0.1', 5000) #socket precisa desta tupla
s.bind(server_address) #socket vincula endpoint servidor e porta de socket
s.listen(1) #espera algum cliente conectar
print("Servidor escutando...")

connection, address = s.accept() #aceita conexão
print('Servidor aceitando conexão...')
data = connection.recv(1024) # método recv recebe mensagem TCP, 1024 é o tamanho do buffer
print(f'Servidor está recebendo: {data.decode('utf-8')}')

if not data:
    connection.sendall(data)

MSG = data.decode('utf-8').upper()
print(f'Mensagem a ser enviada pelo servidor: {MSG}')

connection.sendall(MSG.encode('utf-8')) #formata o dado e codifica antes de enviar

connection.close()
s.close()
