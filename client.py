from socket import *
import json

#Импортировал библиотеку
s = socket(AF_INET,SOCK_STREAM)
host = 'localhost'
port = 8888
addr = (host, port)
#Переменный для удобства
s.connect(addr)
#Соединение с сервером

s.send(b"Hello! \n")
tm = s.recv(1024)

#количество байт

print ("Текущее время: %s" % tm.decode('ascii'))
s.close()
#Закрываем соединенеие