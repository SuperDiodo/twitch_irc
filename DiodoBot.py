import irc
import os
import sys


def clear(): 
    if sys.platform == "linux":
        os.system('clear')
    else:
        os.system("cls")


class message:

    def __init__(self, text: str):
        self.channel = text.split("PRIVMSG").pop().split(":")[0].replace("#", "").replace(" ", "")
        self.message = text.split("PRIVMSG").pop().split(":").pop()
        self.username = text.split(".tmi.twitch.tv")[0].split("@").pop()

    def Print(self):
        print("User: ", self.username)
        print("Channel: ", self.channel)
        print("Message: ", self.message)
        print("\n")

class Bot:

    def __init__(self, channel: str, secret: str, nickname: str):
        self.client = irc.IRC(channel, secret, nickname)
        self.client.sock.send(f"CAP REQ :twitch.tv/tags twitch.tv/commands twitch.tv/membership\r\n".encode('utf-8')) #unused

        clear()

        print("============================")
        print("      " + nickname + " ONLINE")
        print("============================\n")

    def listen_channel(self):

        while True:
            resp = self.client.read()

            if "PRIVMSG"  in resp:
                m = message(resp)
                m.Print()


    def Run(self):
       self.listen_channel()

def Main():

    # Channel where you want to connect
    channel = 'superdiodo'

    # I take it from <https://twitchapps.com/tmi/>
    token = ''

    # Nickname of the twitch account you want to connect with
    nickname = 'diodobot'

    diodobot = Bot(channel, token , nickname)
    diodobot.Run()

Main()
