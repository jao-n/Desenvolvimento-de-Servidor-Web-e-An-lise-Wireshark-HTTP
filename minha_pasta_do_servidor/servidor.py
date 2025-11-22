# Importa o módulo socket
from socket import *
import sys  # Necessário para encerrar o programa

# Cria o socket TCP (orientado à conexão)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepara o socket do servidor
#Fill in start
serverPort = 6789  # Define a porta que o servidor vai escutar
serverSocket.bind(('', serverPort))  # Associa o socket a todas as interfaces de rede na porta definida
serverSocket.listen(1)  # Habilita o socket para aceitar conexões, com uma fila de até 1 conexão pendente
#Fill in end

while True:
    # Estabelece a conexão
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  #Fill in end # Bloqueia e aguarda uma conexão de um cliente. 'addr' contém o IP e porta do cliente.

    try:
        # Recebe a mensagem do cliente (requisição HTTP)
        message = connectionSocket.recv(1024).decode()  #Fill in end # Lê até 1024 bytes da conexão e decodifica de bytes para string
        filename = message.split()[1]  # Extrai o segundo elemento da requisição (ex.: /HelloWorld.html)
        f = open(filename[1:])  # Abre o arquivo, removendo a barra '/' inicial do nome do arquivo
        outputdata = f.read()  #Fill in end # Lê TODO o conteúdo do arquivo e armazena em uma string

        # Envia a linha de status do cabeçalho HTTP
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #Fill in end
        # Envia o conteúdo do arquivo ao cliente
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Fecha a conexão com o cliente
        connectionSocket.close()

    except IOError:
        # Envia mensagem de erro 404 se o arquivo não for encontrado
        #Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        #Fill in end

        # Fecha o socket do cliente
        #Fill in start
        connectionSocket.close()
        #Fill in end

serverSocket.close()
sys.exit()  # Encerra o programa