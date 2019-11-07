import asyncio
import os
import urllib
import mimetypes

class Cookie:
    def __init__(self, pos):
        self.pos = pos
    def change(self, pos):
        self.pos = pos

def createResponse(code=200, type='text/html', charset='utf-8', setCookie=False, path='', length=0, appendlist=''):
    if not hasattr(createResponse, 'cnt'):
        createResponse.cnt = 0
    if code == 200:
        html = [b'HTTP/1.0 200 OK \r\n']
    elif code == 405:
        html = [
            b'HTTP/1.0 405 \r\n',
            b'Content-Type:text/html; charset=utf-8\r\n',
            b'Connection: close\r\n',
            b'\r\n',
            b'<html><h1>405 Method Not Allowed</h1><hr></html>\r\n',
            b'\r\n'
        ]
        return html
    else:
        html = [b'HTTP/1.0', str(code).encode(encoding='utf-8')]
    html.append("Content-Type:{}; charset={}\r\n".format(type, charset).encode(encoding='utf-8'))
    if setCookie:
        html.append("Set-Cookie: local_user=yuh{}\r\n".format(createResponse.cnt).encode(encoding='utf-8'))
        createResponse.cnt += 1
    if length != 0:
        html.append((b'Content-Length:', str(length).encode(encoding='utf-8'), b'\r\n'))
    html.append(b'Connection: close\r\n')
    html.append(b'/r/n')
    if length == 0:
        html.append((b'<html><h1>', str(path).encode(encoding='utf-8'), b'</h1><hr></html>\r\n'))
    html.append(appendlist.encode(encoding='utf-8'))
    return html

def analyser(data):
    data = data.split(' ')
    method
    cookie
    path

if __name__ == '__main__':
    print(createResponse(setCookie=True))
