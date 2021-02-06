from socket import *
from random import *
name, port = 'localhost', 12000

s_soc = socket(AF_INET, SOCK_STREAM)
s_soc.bind((name, port))
s_soc.listen(1)
server_name = "Prince Server"
print("Server Initialized: " + server_name)

server_loop = True

while server_loop:

        con, addr = s_soc.accept()
        name = con.recv(1024).decode()
        data = con.recv(1024).decode()
        
        resp_name = name[10:]
        
        print("Client Name: " + resp_name)
        print("Server name: " + server_name)
        
        random_num = randint(1, 100)
        resp_data_rand = str(random_num)
        
        resp_data_int = int(data)
        resp_data_int = resp_data_int + random_num
        resp_data_sum = str(resp_data_int)
        
        con.send(server_name.encode())
        print("Sent Name")
        con.send(resp_data_rand.encode())
        print("Sent Generated Number")
        con.send(resp_data_sum.encode())
        print("Sent Summed Number")
        con.close()
        server_loop = False
