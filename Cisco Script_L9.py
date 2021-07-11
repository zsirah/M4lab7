import os
import datetime
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import SSHException
from netmiko.ssh_exception import NetmikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException

time = datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")

file = 'SDNR1_BACKUP' + "-" + time + ".conf"

un = input("Enter your username: ")
pw = getpass("Enter your password: ")

dev = {
	'ip': '192.168.166.129',
	'device_type': 'cisco_ios',
	'username': un,
	'password': pw
}

try:
	c = ConnectHandler(**dev)
except(NetMikoTimeoutException):
	print (f"The connection to host {dev['ip']} has timed out")
except (NetmikoAuthenticationException):
	print (f"Incorrect username or password for {dev['ip']}")
except (SSHException):
	print (f"No connection can be made via SSH to {dev['ip']}. Please check configuration") 
	

result = c.send_command('show run')

f = open(file, 'x')

f.write(result)

f.close()

print ('The running-config has been backed-up and saved in your directory')
print ('The script has come to an end')




