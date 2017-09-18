# NetworkSecurity2
601.444 Network Security Fall 2017

I created this new repository because there was something wrong with my virtual box (It does not allow me to open two shells at the same time, which made me hard to test my code for both Server.py and Client.py), so I wrote my code directly on my Mac. Link to my original submission for lab1b on 9/6: https://github.com/SYLLL/NetworkSecurity/blob/master/submission/netsec_fall2017/lab_1b/submission.py

==================================================================================

Comments on Lab1b (The code for Lab1b in this repository is the exact copy of my original submission on 9/6)

1. Besides basic unit tests (two packets are equal/ not equal), some experiments are done:
    a. Intentionally assigning a STRING to an INT field does not affect the packet to behave as a "correct" packet.
    b. Assigning a negative value to an UINT, an ValueError will be thrown.
    c. Using both Deserializer and Deserialize to test all types of packets.

2. I required all iDs of packets to be UINT, and the result to be STRING ("correct" or "incorrect") instead of BOOL.

==================================================================================

Comments on Lab1c:

1. When connection_made is called, Client immediately sends a request to server.
Then Server randomly chooses a word among "South", "North", "East", "West" (save 
the word choice to itself secretly) and sends back the wordLength packet with 
corresponding word length of the word. Then Client makes a random guess based on the given word length. In the end, Server responds to Client with the packet containing if Client was correct. (More details in comments)

2. I've tested my Client and Server programs using event loop. To run:
    Uncomment bottem lines from Server.py and enter command: python3 Server.py
    Uncomment bottem lines from Client.py and enter command: python3 Client.py
    
3. I've run unit tests on Client.py and Server.py:
    Enter command: python3 submission.py

4. I've tested the states for each Client's protocol instance and Server's 
protocol instance. For example, when connection is made, both the states 
change to 1, and in the end, both the states change to 4 since each of them
call data_received twice and connection_lost once.

==================================================================================

Comments on Lab1d:

1. For some reason, Server does not get Client's first packet even if connection is established, so I have
to make Client sleep for 5 seconds before sending a new packet, which is added in the bottom lines of Client.py

2. To run:
    python3 Server.py
    python3 Client.py

3. To kill:
    press control+c

==================================================================================

Comments on Lab1e:

1. Since the first packet not received bug is fixed, I removed the resend part when EchoClientProtocol is initialized.

2. Although FirstPassingThroughProtocol is chained before SecondPassingThroughProtocol, SecondPassingThroughProtocol is in a lower layer, which is first passed through when I test
with my programs.

3. To run:
    python3 Server.py
    python3 Client.py

4. To kill:
    press control+c