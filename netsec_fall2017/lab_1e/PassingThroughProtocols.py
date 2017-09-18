# two layers of passing through protocols
import asyncio
import playground
from playground.network.common import StackingProtocol, StackingTransport, StackingProtocolFactory

# Layer 1
class FirstPassingThroughProtocol(StackingProtocol):
    def __init__(self):
        print('FirstPassingThroughProtocol initialized')
        print('')
        self.transport = None
        super().__init__

    def connection_made(self, transport):
        print('FirstPassingThroughProtocol connection made')
        print('')
        self.transport = transport
        higherTransport = StackingTransport(self.transport)
        self.higherProtocol().connection_made(higherTransport)

    def data_received(self, data):
        print('FirstPassingThroughProtocol data received')
        print('')
        self.higherProtocol().data_received(data)

    def connection_lost(self, exc):
        print('FirstPassingThroughProtocol connection lost')
        print('')
        self.transport = None
        self.higherProtocol().connection_lost(exc)

# Layer 2
class SecondPassingThroughProtocol(StackingProtocol):
    def __init__(self):
        print('SecondPassingThroughProtocol initialized')
        print('')
        self.transport = None
        super().__init__

    def connection_made(self, transport):
        print('SecondPassingThroughProtocol connection made')
        print('')
        self.transport = transport
        higherTransport = StackingTransport(self.transport)
        self.higherProtocol().connection_made(higherTransport)

    def data_received(self, data):
        print('SecondPassingThroughProtocol data received')
        print('')
        self.higherProtocol().data_received(data)

    def connection_lost(self, exc):
        print('SecondPassingThroughProtocol connection lost')
        print('')
        self.transport = None
        self.higherProtocol().connection_lost(exc)
