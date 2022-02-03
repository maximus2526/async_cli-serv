# python3
import ast  # Change str - code literaly
import asyncio
import sys

counter = 0


async def run_server(host, port):
    server = await asyncio.start_server(serve_client, host, port)
    await server.serve_forever()


async def serve_client(reader, writer):
    global counter
    cid = counter
    counter += 1  # Потоко-безопасно, так все выполняется в одном потоке
    print(f'Client #{cid} connected')
    request = await read_request(reader)
    request = ast.literal_eval(request.decode('utf-8'))
    print(request)
    hub_meta = request['data'].split('%%')[0].split('&&')
    device_meta = request['data'].split('%%')[1].split('&&')

    dict_out = {
        'request_id': request['request_id'],
        'data': {
            hub_meta[0]: {'name': request['data'].split('%%')[0].split("&&")[2],
                          'id': request['data'].split('%%')[0].split("&&")[4]},
            device_meta[0]: {'name': request['data'].split('%%')[1].split("&&")[2],
                             'id': request['data'].split('%%')[1].split("&&")[4]},
        }
    }
    await write_response(writer, str(dict_out).encode("utf-8"), cid)


async def read_request(reader):
    request = await reader.read(n=-1)
    return request


async def write_response(writer, response, cid):
    print(response)
    writer.write(response)
    writer.close()
    print(f'Client #{cid} has been served')


if __name__ == '__main__':
    asyncio.run(run_server('127.0.0.1', 5036))
