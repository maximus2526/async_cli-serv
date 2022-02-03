import random
import socket
import json
import ast  # Change str - code literally
import asyncio
import time

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

server.bind(("localhost", 5917))
server.listen(100)


def accept():
    server.accept()


accept()
while True:
    data_output = server.recv(1024).decode("utf-8")
    data_output = ast.literal_eval(data_output)
    hub_meta = data_output['data'].split('%%')[0].split('&&')
    device_meta = data_output['data'].split('%%')[1].split('&&')

    dict_out = {
        'request_id': data_output['request_id'],
        'data': {
            hub_meta[0]: {'name': data_output['data'].split('%%')[0].split("&&")[2],
                          'id': data_output['data'].split('%%')[0].split("&&")[4]},
            device_meta[0]: {'name': data_output['data'].split('%%')[1].split("&&")[2],
                             'id': data_output['data'].split('%%')[1].split("&&")[4]},
        }
    }

    server.send(str(dict_out).encode('utf-8'))
