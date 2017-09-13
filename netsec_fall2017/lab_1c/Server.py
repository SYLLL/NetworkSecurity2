# Server side
import asyncio
from Packets import RequestWordLength, WordLength, GuessWord, GuessResult
from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, STRING
from random import randint

class EchoServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None
        self.status = 0

    def connection_made(self, transport):
        self.transport = transport
        self._deserializer = PacketType.Deserializer()
        peername = transport.get_extra_info('peername')
        print('Connection is made from {}'.format(peername))
        print('')
        self.status += 1

    def data_received(self, data):
        self._deserializer.update(data)
        for pkt in self._deserializer.nextPackets():
            self.processPacket(pkt)
        self.status += 1

    def connection_lost(self, exc):
        print('Connection is closed')
        self.transport = None
        self.status += 1

    def processPacket(self, pkt):
        if isinstance(pkt, RequestWordLength):
            print('Received RequestWordLength packet from client:')
            print('Fields of this packet are empty')
            print('')
            self.sendWordLength(pkt)
        elif isinstance(pkt, GuessWord):
            print('Received GuessWord packet from client:')
            print('word:', pkt.word)
            print('iD:', pkt.iD)
            print('')
            self.sendGuessResult(pkt)
        else:
            print("Error: received packet type not defined.")

    def sendWordLength(self, pkt):
        wdLength = WordLength()
        wdLength.iD = 1024
        # Randomly choose a correct word for client
        if randint(0,3) == 0:
            wdLength.wordLength = 4
            self.correctword = "East"
        elif randint(0,3) == 1:
            wdLength.wordLength = 4
            self.correctword = "West"
        elif randint(0,3) == 1:
            wdLength.wordLength = 5
            self.correctword = "North"
        else:
            wdLength.wordLength = 5
            self.correctword = "South"
        self.transport.write(wdLength.__serialize__())
        print('Sent WordLength packet to client:')
        print('wordLength:', wdLength.wordLength)
        print('iD:', wdLength.iD)
        print('')

    def sendGuessResult(self, pkt):
        guessResult = GuessResult()
        guessResult.iD = pkt.iD
        guessedWord = pkt.word
        # Check if the client's guess is correct
        if guessedWord == self.correctword:
            guessResult.result = "correct"
        else:
            guessResult.result = "incorrect"
        self.transport.write(guessResult.__serialize__())
        print('Sent GuessResult packet to client:')
        print('result:', guessResult.result)
        print('iD:', guessResult.iD)
        print('')

'''
loop = asyncio.get_event_loop()
coro = loop.create_server(lambda: EchoServerProtocol(), '127.0.0.1', 8888)
server = loop.run_until_complete(coro)
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
'''