import socket
import json

#configs do servidor

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

#Criar socket

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#vincular o socket o endereco e porta

servidor_socket.bind((SERVER_IP,SERVER_PORT))

# outra forma de exibir dados recebidos (forma 2)

print('Dados recebidos:')
print(dados['nome'])
print(dados['idade'])
print(dados['email'])

# mais uma forma de exibir dados recebidos (forma 3)

print(f'Dados recebidos. Nome: {dados['nome']}. Idade: {dados['idade']}. Email: {dados['email']} ')

#fechar conexão e socket do servidor

conexao.close()
servidor_socket.close()

#aguardar conexoes

servidor_socket.listen()
print('Aguardando conexões...')

#aceitar conexão

conexao, endereco = servidor_socket.accept()
print(f'conectado a {endereco}')

#receber dados JSON

dados_json = conexao.recv(1024).decode('utf-8')
dados = json.loads(dados_json)

#exibir dados recebidos (forma 1)

print('Dados recebidos:')
print(dados)