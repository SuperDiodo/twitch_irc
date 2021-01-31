# twitch_irc
Simple IRC class for a Twitch bot. There is also a bot example called "Diodobot".

## IRC class
It is composed by:
-   `connect`: connect to a server using the twitch account secret, the nickname and the target channel name
-   `read`: read a message from the connection
-   `write`: write something in the channel as a PRVMSG
-   `close`: close the socket connection

## Usage
1.  Make sure you have `pip` installed for extra modules if you want to include them in `requirements.txt`
2.  Change the channel, nickname and secrete as in the main of `DiodoBot.py`
3.  `python.exe ./Diodobot.py`
