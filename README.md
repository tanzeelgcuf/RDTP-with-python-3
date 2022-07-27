# RDTP-with-python-3
implementing a reliable transport protocol over UDP in Python 3. The
protocol will mostly follow rdt 3.0, so it must support timeouts (of 1.5 seconds), and will ACK segments. If
a corrupted or out of order segment is received, we will use a NAK.
In our program, the client will send data to a server, and there will be no handshaking. Instead the arguments
(see below) will specify details such as initial sequence numbers. We will assume that the client sends data
to the server, and the server sends ACK/NAK messages back, but the server will not send data to the client
(i.e unidirectional data transfer).
