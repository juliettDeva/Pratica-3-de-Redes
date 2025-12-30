import socket
import json

#Dados do usuario em formato de dicionario

usuario = {
    'user': None,
    'data' : None,
    
}

usuario['user'] = input('Digite nome de usuario: ')
usuario['data'] = input('Digite mensagem a ser enviada: ')

# converter dicionario em string JSON

usuario_json = json.dumps(usuario)

# configs do servidor

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

#criar socket

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conectar ao servidor

cliente_socket.connect((SERVER_IP, SERVER_PORT))

#enviar JSON

cliente_socket.send(usuario_json.encode('utf-8'))

#fechar o socket do cliente

cliente_socket.close()