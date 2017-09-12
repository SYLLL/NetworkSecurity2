# NetworkSecurity2
601.444 Network Security Fall 2017

I created this new repository because there was something wrong with my virtual box, so I wrote my code directly on my Mac. Link to my original submission for lab1b on 9/6: https://github.com/SYLLL/NetworkSecurity/blob/master/submission/netsec_fall2017/lab_1b/submission.py

==================================================================================

Comments on Lab1b:

1. Besides basic unit tests (two packets are equal/ not equal), some experiments are done:
    a. Intentionally assigning a STRING to an INT field does not affect the packet to behave as a "correct" packet.
    b. Assigning a negative value to an UINT, an ValueError will be thrown.
    c. Using both Deserializer and Deserialize to test all types of packets.

2. I required all iDs of packets to be UINT, and the result to be STRING ("correct" or "incorrect") instead of BOOL.

Comments on Lab1c:

1. I've tested my Client and Server programs using event loop. To run:
    Uncomment bottem lines from Server.py and enter command: python3 Server.py
    Uncomment bottem lines from Client.py and enter command: python3 Client.py
    
2. I've run unit tests on Client.py and Server.py:
    Enter command: python3 submission.py

