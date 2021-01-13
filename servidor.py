# coding: utf-8
import socket

try:
    
    #socket.socket == realizar todo o procedimento | socket.DF_NET == ipv4 | SOCK_STREAM == TCP
    servidor = socket.socket()
    
    #bind serve para amarrar o ip e a porta
    servidor.bind(('', 3315))
    
    #Número de clientes que vão ficar em filas
    servidor.listen( 5 )

    

    #Iniciando um laço de repetição para a porta sempre ficar escutando e esperando o cliente
    while True:
        
        
        
        #Aceitando conexão com o cliente ao se conectar, receberá o ip e a porta
        client, address = servidor.accept()
        
        print('Cliente conectado')

except: print('Servidor desconectado da Rede')