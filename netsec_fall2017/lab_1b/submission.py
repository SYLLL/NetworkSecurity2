# Experiment: ValueError will be thrown if a negative number 
# is assigned to unsigned int
# I'm assuming all iDs are unsigned int, and the result field 
# in GuessResult packet is either "correct" or "incorrect"
# in STRING format (instead of BOOL type)
from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, STRING

# Client sends request word length packet.
class RequestWordLength(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.student_SuyiLiu.RequestWordLength"
    DEFINITION_VERSION = "1.0"

    FIELDS = []

# Server responds with a packet with a word length.
class WordLength(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.student_SuyiLiu.WordLength"
    DEFINITION_VERSION = "1.0"

    FIELDS = [
        ("wordLength", UINT32),
        ("iD", UINT32)
        ]

# Client sends a packet with the guess of direction.
class GuessWord(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.student_SuyiLiu.GuessWord"
    DEFINITION_VERSION = "1.0"

    FIELDS = [
        ("word", STRING),
        ("iD", UINT32)
        ]

# Server sends the result whether the guess is correct.
class GuessResult(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.student_SuyiLiu.GuessResult"
    DEFINITION_VERSION = "1.0"

    FIELDS = [
        ("result", STRING),
        ("iD", UINT32)
        ]

def basicUnitTest():
    print ('Now running unit tests.')
    
    # Verify 1st packet remains the same
    packet1 = RequestWordLength()
    packet1Bytes = packet1.__serialize__()
    packet1d = RequestWordLength.Deserialize(packet1Bytes)
    assert packet1 == packet1d

    # Verify 2nd packet remains the same
    packet2 = WordLength()
    packet2.wordLength = 4
    packet2.iD = 32768
    packet2Bytes = packet2.__serialize__()
    packet2d = WordLength.Deserialize(packet2Bytes)
    assert packet2 == packet2d

    # Verify 2nd packet remains the same if a STRING is assigned to
    # wordLength
    packet2b = WordLength()
    packet2b.wordLength = '4'
    packet2b.iD = 32768
    packet2bBytes = packet2b.__serialize__()
    packet2bd = WordLength.Deserialize(packet2bBytes)
    assert packet2b == packet2bd

    # Verify packet2b equals packet2 even their wordLength types are
    # not the same
    assert packet2 == packet2b

    # Verify 3rd packet remains the same
    packet3 = GuessWord()
    packet3.word = "East"
    packet3.iD = 32768
    packet3Bytes = packet3.__serialize__()
    packet3d = GuessWord.Deserialize(packet3Bytes)
    assert packet3 == packet3d

    # Verify 4th packet remains the same
    packet4 = GuessResult()
    packet4.result = "correct"
    packet4.iD = 32768
    packet4Bytes = packet4.__serialize__()
    packet4d = GuessResult.Deserialize(packet4Bytes)
    assert packet4 == packet4d    

    # Verify 1st packet is not the same as 2nd packet
    assert packet1 != packet2

    # Verify packets don't change using Deserializer
    packeta = RequestWordLength()
    
    packetb = WordLength()
    packetb.wordLength = 5
    packetb.iD = 65536
    
    packetc = GuessWord()
    packetc.word = "West"
    packetc.iD = 65536
    
    packetd = GuessResult()
    packetd.result = "incorrect"
    packetd.iD = 65536

    pktBytes = packeta.__serialize__() + packetb.__serialize__() + packetc.__serialize__() + packetd.__serialize__()
    deserializer = PacketType.Deserializer()
    deserializer.update(pktBytes)
    for packet in deserializer.nextPackets():
        assert packet == packeta or packet == packetb or packet == packetc or packet == packetd

    # Verify two WordLength packets are not equal because iDs are not equal.
    packet2_first = WordLength()
    packet2_first.wordLength = 4
    packet2_first.iD = 1024
    packet2_second = WordLength()
    packet2_second.wordLength = 4
    packet2_second.iD = 2048
    assert packet2_first != packet2_second

    # Verify two GuessWord packets are not equal because words are not equal.
    packet3_first = GuessWord()
    packet3_first.word = "East"
    packet3_first.iD = 1024
    packet3_second = GuessWord()
    packet3_second.word = "North"
    packet3_second.iD = 1024
    assert packet3_first != packet3_second

    # Verify two GuessResult packets are not equal because results are not equal.
    packet4_first = GuessResult()
    packet4_first.result = "correct"
    packet4_first.iD = 2048
    packet4_second = GuessResult()
    packet4_second.result = "incorrect"
    packet4_second.iD = 2048
    assert packet4_first != packet4_second

    print ('All unit tests passed.')
    
def main():
    basicUnitTest()

if __name__ == "__main__":
    main()
