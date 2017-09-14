# Client side
import asyncio
import playground
from Packets import RequestWordLength, WordLength, GuessWord, GuessResult
from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, STRING
from random import randint
import time

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None
        self.loop = loop
        self.status = 0

    def connection_made(self, transport):
        print('Connection is made')
        print('')
        self.transport = transport
        self._deserializer = PacketType.Deserializer()
        self.status += 1

    def data_received(self, data):
        self._deserializer.update(data)
        for pkt in self._deserializer.nextPackets():
            self.processPacket(pkt)
        self.status += 1

    def connection_lost(self, exc):
        print('Connection is closed by the server')
        self.transport = None
        self.status += 1

    def processPacket(self, pkt):
        if isinstance(pkt, WordLength):
            print('Received WordLength packet from server:')
            print('wordLength:', pkt.wordLength)
            print('iD:', pkt.iD)
            print('')
            self.sendGuessWord(pkt)
        elif isinstance(pkt, GuessResult):
            print('Received GuessResult packet from server:')
            print('result:', pkt.result)
            print('iD:', pkt.iD)
            print('')
            self.transport.close()
        else:
            print("Error: received packet type not defined.")
            self.transport.close()

    def sendRequestWordLength(self):
        rqstWordLength = RequestWordLength()
        self.transport.write(rqstWordLength.__serialize__())
        print('Sent RequestWordLength packet to server:')
        print('Fields of this packet are empty')
        print('')

    def sendGuessWord(self, pkt):
        wdLength = pkt.wordLength
        guessWord = GuessWord()
        guessWord.iD = pkt.iD
        # Make a random guess
        if randint(0,1) == 0:
            if wdLength == 4:
                guessWord.word = "East"
            elif wdLength == 5:
                guessWord.word = "North"
            else:
                print("Error: received word length not allowed.")
        else:
            if wdLength == 4:
                guessWord.word = "West"
            elif wdLength == 5:
                guessWord.word = "South"
            else:
                print("Error: received word length not allowed.")
        self.transport.write(guessWord.__serialize__())
        print('Sent GuessWord packet to server:')
        print('word:', guessWord.word)
        print('iD:', guessWord.iD)
        print('')

loop = asyncio.get_event_loop()
#coro = loop.create_connection(lambda: EchoClientProtocol(), '127.0.0.1', 8888)
coro = playground.getConnector().create_playground_connection(lambda: EchoClientProtocol(), '20174.1.1.1', 888)
transport, c = loop.run_until_complete(coro)
c.sendRequestWordLength()
time.sleep(5)
c.sendRequestWordLength()
loop.run_forever()
loop.close()
