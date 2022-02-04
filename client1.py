import socket
import ast  # Change str - code literally

req = '{ "request_id": "01", "data": "Hub&&name&&qwe&&id&&123&&%%Device&&name&&wqe&&id&&234&&"}'

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "localhost"
PORT = 5036
connection.connect((IP, PORT))
connection.send(req.encode("utf-8"))
resp_json = connection.recv(1024)
print("Received message: " + str(ast.literal_eval(resp_json.decode('utf-8'))))
connection.close()
