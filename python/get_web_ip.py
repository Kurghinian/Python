import socket
from time import sleep as s
webName = input("Enter Website Domain Example(Google.com) -  ")
get_ip = socket.gethostbyname(webName)
print(webName, "IP -", get_ip)
#Created By Kurghinian 
s(1)
print("Thank You !!")