import asyncio
import ast  # Change str - code literally


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 5036)
    message = message.encode('utf-8')
    print(f'Send: {message!r}')
    writer.write(message)
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()


async def main():
    msg = '{"request_id": "01", "data": "Hub&&name&&qwe&&id&&123&&%%Device&&name&&wqe&&id&&234&&"}'
    await asyncio.gather(
        tcp_echo_client(msg), tcp_echo_client(msg), tcp_echo_client(msg), tcp_echo_client(msg), tcp_echo_client(msg),
    )

asyncio.run(main())

