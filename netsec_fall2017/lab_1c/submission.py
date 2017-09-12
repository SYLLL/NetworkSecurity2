# Runs the unit tests
import asyncio
from Client import EchoClientProtocol
from Server import EchoServerProtocol
from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToStorageStream
from playground.network.testing import MockTransportToProtocol
from Packets import RequestWordLength, WordLength, GuessWord, GuessResult
from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, STRING

def basicUnitTest():
    s = EchoServerProtocol()
    c = EchoClientProtocol()
    transportToServer = MockTransportToProtocol(s)
    transportToClient = MockTransportToProtocol(c)
    s.connection_made(transportToClient)
    c.connection_made(transportToServer)
    
    print ('Unit tests passed.')

if __name__ == "__main__":
    basicUnitTest()