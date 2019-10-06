import asyncio
import socket
async def echo(reader, writer):
    client = writer.get_extra_info('peername')
    while True:
        data = await reader.readline()
        message = data.decode().split(' ')
        print(data)
        writer.write(data)
        if data == b'\r\n':
            break

    await writer.drain()
    writer.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(echo, '127.0.0.1', 5555, loop=loop) 
    server = loop.run_until_complete(coro)
    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()