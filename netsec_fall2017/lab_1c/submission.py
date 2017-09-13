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
    cTransport, sTransport = MockTransportToProtocol.CreateTransportPair(c, s)
    # Both client protocol and server protocols' states are 0 at this time
    assert s.status == 0
    assert c.status == 0
    s.connection_made(sTransport)
    c.connection_made(cTransport)
    # Both client protocol and server protocols' states change to 3 at this time
    assert s.status == 3
    assert c.status == 3
    s.connection_lost(None)
    c.connection_lost(None)
    # Both client protocol and server protocols' states are 4 when they 
    # are both closed at this time
    assert s.status == 4
    assert s.status == 4
    print ('Unit tests passed.')

if __name__ == "__main__":
    basicUnitTest()