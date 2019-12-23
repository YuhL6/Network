import socket
import dnslib
import selectors
from pytun import TunTapDevice


class Client:
    def __init__(self):
        self.selectors = selectors.DefaultSelector()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tun = TunTapDevice(name='mytun', flags=IFF_TUN)
        self.selectors.register(self.tun, selectors.EVENT_READ, self.packetSender)
        self.selectors.register(self.sock, selectors.EVENT_READ)

    def packetSender(self, tun, mask):
        data = tun.read(100)
        data = self.dnsAssemble(data)
        self.sock.sendto(data, ('120.78.166.34', 53))

    def dnsAssemble(self, data):
        packet = dnslib.DNSRecord.question("{}group-17.cs305.fun".format(data), "TXT")
        return packet.pack()

    def packetReader(self, conn, mask):
        data = conn.read(1024).decode()
        packet = dnslib.DNSRecord.parse(data)
        msg = packet.questions
        self.tun.write(msg)

    def run(self):
        while True:
            events = self.selectors.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)


if __name__ == '__main__':
    client = Client()
    client.run()




