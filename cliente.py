import socket
import json

#Dados do usuario em formato de dicionario

usuario = {
    'nome': 'Amora',
    'idade' : 7,
    'email' : 'amora@example.com'
}

# converter dicionario em JSON

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