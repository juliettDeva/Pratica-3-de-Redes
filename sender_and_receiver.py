import socket
import struct

def sender():
    #configurando multicast
    MULTICAST_GROUP = '224.3.29.71'
    MULTICAST_PORT = 5007

    #criando socket 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    ttl = struct.pack('b', 1) #empacota em formato byte o valor 1

    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    #enviar mensagem
    s.sendto(f'Olá, grupo Multicast!'.encode('utf-8'), (MULTICAST_GROUP, MULTICAST_PORT))

def receiver():
    #configs
    MULTICAST_GROUP = '224.3.29.71'
    MULTICAST_PORT = 5007

    #criar socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', MULTICAST_PORT))

    # grupo multicast
    group = socket.inet_aton(MULTICAST_GROUP)
    mreq = struct.pack('4sl', group, socket.INADDR_ANY)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    #receber e exibir mensagens

    while True:
        print('Receptor aguardando mensagens...')
        data, addr = s.recvfrom(1024)
        print(f'Recebido de {addr}: {data.decode('utf-8')}')
