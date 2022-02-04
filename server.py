# python3
import asyncio
import json
import random

counter = 0


class Server:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 5036

    async def run(self):
        serv = await asyncio.start_server(self.handler, self.host, self.port)
        await serv.serve_forever()

    async def handler(self, reader, writer):
        await asyncio.sleep(random.randint(1, 5))
        print(f'Client connected')
        request = await reader.read(100)
        print(f"Request :: {request}")
        response = self._parse_request(request)
        writer.write(response)
        print(f"Response :: {response}")
        writer.close()

    @staticmethod
    def _parse_request(request):
        request = json.loads(request.decode('utf-8'))
        parsed = tuple(o.split("&&")[:-1] for o in request["data"].split("%%"))
        response = {obj[0]: dict(zip(obj[1::2], obj[2::2])) for obj in parsed}
        response.update({"request_id": request["request_id"]})
        return json.dumps(response).encode("utf-8")


if __name__ == '__main__':
    server = Server()
    asyncio.run(server.run())
