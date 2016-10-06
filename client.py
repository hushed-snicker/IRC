#!/usr/bin/env python
import socket, select, string, sys
from time import sleep

##########
# Config #
##########

defHost = 'localhost'	#default host for -d
defPort = 9395		#default port for -d
nick = 'test'		#default nick used
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

##############
# End Config #
##############
# ToDo #
########
#'''
#___Compliance
#'''

#'''
#	Function: Prompts for nickname
#	Return Value: None
#'''
def prompt_nick():
#	print('prompt_nick()')

	global nick

	if nick:	#if there is a nick entered in the config
		print('Using preset nick of %s.') % nick
	elif nick == '':
		nick = raw_input('Please enter username: ')
	else:
		print('Send username first on connect')
'''
	Function: Standard prompt after prompt_nick
	Return Value: Returns users input
	Retrun Type: String
'''
def prompt() :		#prompts for input. Returns input as string
#	print('prompt()')

	global nick

	msg = raw_input(nick + '> ')
	return msg

'''
	Function: Connect to host
	Return Value: None
'''
def connect():
#	print('connect()')

	global s

	try:
		s.connect((host, port))
	except:
		print("Unable to connect")
		sys.exit()

	print("Connected to remote host.")

'''
	Function: Main Loop
	Return Value: none
'''
def loop():
#	print('loop()')

	global s

	while 1:
#		print('while 1:')
		socket_list = [sys.stdin, s]

		#Get the list sockets which are readable
#		print('socket list get')
		msg = prompt()
		read_sockets, write_sockets, error_sockets = socket_list , [], []

		for sock in read_sockets:
#			print('start for loop')
			#incoming message from remote server
			if sock == s:
#				print('Check for message')
				data = sock.recv(4096)

				if data:
					print(data)
			#user entered a message
			else:
#				print('Send message')
#				print('Message is : %s') % msg
				s.send(msg)

#main function

if __name__ == "__main__":

	# command arg parse
	if len(sys.argv) == 2:		#Single argument switches
		if sys.argv[1] == '-d':
			host = defHost
			port = defPort
	elif len(sys.argv) == 3:	#Standard use of program
		host = sys.argv[1]
		port = int(sys.argv[2])
	else:
		print 'Usage : python client.py hostname port'
		sys.exit()


	# connect to remote host
	connect()

	# ask for nick
	prompt_nick()

	# True main loop
	loop()
