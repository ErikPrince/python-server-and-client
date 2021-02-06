from socket import *
s_name, s_port = 'localhost', 12000

c_soc = socket(AF_INET, SOCK_STREAM)
c_soc.connect((s_name, s_port))
print('Connected to Remote Server')

name = 'Erik Prince'
client_name = "Client of " + name
print(client_name)
data = input("Input an integer between 1 and 100.")
c_soc.send(client_name.encode())
c_soc.send(data.encode())
print('Data sent... waiting for the response.')

resp_name = c_soc.recv(1024)
print('Server Name: ', resp_name.decode())
resp_rand = c_soc.recv(1024)
print('Generated Number: ', resp_rand.decode())
resp_data = c_soc.recv(1024)
print('Sum of Numbers: ', resp_data.decode())
c_soc.close()

