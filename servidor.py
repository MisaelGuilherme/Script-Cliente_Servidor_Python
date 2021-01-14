# coding: utf-8
import socket

try:
    
    #socket.socket == realizar todo o procedimento | socket.DF_NET == ipv4 | SOCK_STREAM == TCP
    servidor = socket.socket()
    
    #bind serve para amarrar o ip e a porta
    servidor.bind(('', 3315))
    
    #Número de clientes que vão ficar em filas
    servidor.listen( 5 )

    print('Servidor ligado - porta: 3315')
    
    print('Aguardando conexão . . .')
    print('')
    
    #Aceitando conexão com o cliente ao se conectar, receberá o ip e a porta
    client, ender = servidor.accept()
    lista = []
    lista.append(ender)
    print(lista)

    #Iniciando um laço de repetição para a porta sempre ficar escutando e esperando o cliente
    while True:

        print('Cliente conectado')
        print('')
        
        data = client.recv(1024)
        
        if not data:
            print('Fechando a conexão')
            print('')
            client.close()
            break
        
        msgRecebe = data.decode()
        
        msgEnviar = 'Você digitou '+str(msgRecebe)
        
        client.sendall(msgEnviar.encode())

except Exception as erro: 
    print('Servidor desconectado da Rede')
    print(erro)