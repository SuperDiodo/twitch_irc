import irc
import threading
from emoji import demojize
import re
from gtts import gTTS
import playsound
import os
import time
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

    def __init__(self, channel: str):
        self.client = irc.IRC('CHANNEL_SECRET', channel)
        self.client.sock.send(f"CAP REQ :twitch.tv/tags twitch.tv/commands twitch.tv/membership\r\n".encode('utf-8')) #unused
        
        self.messages_tts = []

        self.commands_periodic = int(input("Commands period in minutes: "))
        self.commercial_period = int(input("Commercial period in minutes: "))
        self.commercial_lenght = int(input("Commercial lenght in seconds: "))

        clear()

        print("============================")
        print("      DIODOBOT ONLINE")
        print("============================\n")

    def listen_channel(self):

        while True:
            resp = self.client.read()
            print(resp)

            if "PRIVMSG"  in resp:
                m = message(resp)
                m.Print()

                if "!tts" in m.message:
                    text = "Messaggio da" +  m.username +  ": " +  m.message.replace("!tts", "")
                    self.messages_tts.append(text)

    def tts(self):

        while True:
            for __ in self.messages_tts:
                myobj = gTTS(text = self.messages_tts.pop(0), lang = "it", slow = False)
                myobj.save("message.mp3")
                playsound.playsound("message.mp3")
                os.remove("message.mp3")

            time.sleep(1)

    def timer(self):

        timer = 0

        while True:
            time.sleep(1)
            timer += 1

            if timer == self.commercial_period*60 - 10:
                self.client.write("Tra 10 secondi ci sarà una pubblicità, supporta lo streamer guardandola! <3")

            if timer == self.commercial_period*60:
                self.client.write("!commercial " + str(self.commercial_lenght))

            if timer == self.commands_periodic*60:
                self.client.write("Usa '!discord' ed entra nel canale discord di SuperDiodo! HeyGuys")
                self.client.write("Vuoi sapere come si chiama SuperDiodo online? Usa '!id' ! FutureMan")
                self.client.write("Con il comando '!tts' puoi far leggere i tuoi messaggi da un bot :)")
                self.client.write("Hai già visto le ricompense punti canale? VirtualHug")
           
            ## if timer reaches 12h then reset
            if timer == 43200:
                timer = 0

    def Run(self):

        self.listen_thread = threading.Thread(target=self.listen_channel)
        self.tts_thread = threading.Thread(target=self.tts)
        self.timer_thread = threading.Thread(target=self.timer)
        self.listen_thread.start()
        self.tts_thread.start()
        self.timer_thread.start()

def Main():
    diodobot = Bot("superdiodo")
    diodobot.Run()

Main()