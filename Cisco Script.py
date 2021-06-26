import os
import datetime
from netmiko import ConnectHandler
from getpass import getpass

time = datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")

file = 'SDNR1' + "-" + time + ".conf"

un = input("Enter your username: ")
pw = getpass("Enter your password: ")

dev = {
	'ip': '192.168.166.129',
	'device_type': 'cisco_ios',
	'username': un,
	'password': pw
}

c = ConnectHandler(**dev)

result = c.send_command('show run')

f = open(file, 'x')

f.write(result)
f.close()


