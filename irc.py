import socket

class IRC:

    def __init__(self, secret: str, channel_name: str):
        self.server = 'irc.chat.twitch.tv'
        self.port = 6667
        self.nickname = 'diodobot'
        self.token = secret
        self.channel = '#' + channel_name
        self.sock = socket.socket()
        self.sock.connect((self.server, self.port))
        self.sock.send(f"PASS {self.token}\r\n".encode('utf-8'))
        self.sock.send(f"NICK {self.nickname}\r\n".encode('utf-8'))
        self.sock.send(f"JOIN {self.channel}\r\n".encode('utf-8'))
        self.sock.recv(2048).decode('utf-8')
        self.sock.recv(2048).decode('utf-8')


    def write(self, message: str):
        self.sock.send (('PRIVMSG '+ self.channel + ' : ' + message + '\r\n').encode('utf-8'))


    def read(self):
        resp = self.sock.recv(2048).decode('utf-8')

        if resp.startswith('PING'):
            self.sock.send("PONG\n".encode('utf-8'))

        return resp

    def close():
        self.sock.close()