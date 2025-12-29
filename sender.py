import socket
import struct

#configurando multicast
MULTICAST_GROUP = '224.3.29.71'
MULTICAST_PORT = 5007

#criando socket 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

ttl = struct.pack('b', 1) #empacota em formato byte o valor 1

s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

#enviar mensagem

s.sendto(f'Olá, grupo Multicast!'.encode('utf-8'), (MULTICAST_GROUP, MULTICAST_PORT))

'''
protocolo usado é IPPROTO_UDP para comunicação usando o protocolo UDP.

A variável ttl serve para configurar o TTL (Time to Live) para os pacotes multicast que serão enviados. TTL é um número que limita a vida útil de um pacote na rede. Você está usando a função struct.pack() para empacotar o valor 1 como um único byte ('b') para definir o TTL como 1. Isso significa que os pacotes multicast serão entregues apenas à rede local. O uso de TTL controla até que ponto a mensagem será entregue na rede e limita sua propagação.
Para entender mais, pesquisa sobre TTL e roteamento


'''