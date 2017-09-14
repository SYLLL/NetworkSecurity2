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