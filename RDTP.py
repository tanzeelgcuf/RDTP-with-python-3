# Local server test, Stop and wait with 5 messages starting at 210
# First run server (listening on port 5555) - note that server timeout will start counting immediately!
# python3 PA2_provided.py SW 5555 5556 5 1 210 localhost server
# In a second terminal run client (listening on port 5556)
# python3 PA2_provided.py SW 5555 5556 5 1 210 localhost client

import sys  # Used for sys.argv, sys.exit()
import os  # Used for os.path.isfile()
import time  # Useful for timestamping in prints
import socket  # Useful for sockets
import select  # Useful for select (handle timeout and reading - see lecture notes)

# Checksum calculation function
def checksum(data):
    csum = 0

    # TODO: Actually do the wrap-around addition of 16-bit "words"
    print("checksum() implementation incomplete!", flush=True)
    sys.exit(-1)

    # Compute the 1s complement
    ones_comp = ~csum & (2 ** 16 - 1)  # Mask so that we don't pick up a weird sign issue
    return ones_comp


# You do not need to use this class, but you should probably use an object to represent messages
class Message:
    def __init__(self):
        self.data = ""
        self.seqno = 0
        self.ackno = 0
        self.ACK = False
        self.csum = 0
        print("Message class implementation incomplete", flush=True)
        sys.exit(-1)

    # TODO: Finish me


# gbn will be true if GBN mode, false if SW mode
def client(gbn, server_port, client_port, num_messages, N, isn, remote_host):
    # Important: When using bind, use an empty string for the hostname and just use the port number!
    # TODO: Write me
    print("Function client() not yet written!", flush=True)
    sys.exit(-1)


def server(gbn, server_port, client_port, remote_host, num_messages, N, isn):
    # Important: When using bind, use an empty string for the hostname and just use the port number!
    # TODO: Write me
    print("Function server() not yet written!", flush=True)
    sys.exit(-1)


# This function should not need any changes
def print_usage():
    print(
        "Proper usage is {} [mode] [server port] [client port] [number of messages] [N] [ISN] [remote host] [server/client]".format(
            sys.argv[0]))
    print("[mode] is either 'SW' or 'GBN'")
    print("\tSW - Stop and Wait protocol (ignores N)")
    print("\tGBN - Go Back N protocol")
    print(
        "[server port] is the port number for the server to listen on (for receiving data) and send ACKs/NAKs on.")
    print("[client port] is the port number for the client to listen on (for receiving ACK/NAKs) and send data on.")
    print("[number of messages] is the number of messages the client will send.")
    print("[N] is the size of the sliding window. For SW this will always be 1 and may be safely ignored.")
    print("[ISN] is the initial sequence number to use.")
    print("[remote host] is the name of the remote host to connect to. Only used by the client.")
    print("[server/client] determines what mode the program should run in")
    print("\tserver - receive data, send ACK/NAKs")
    print("\tclient - Send data, receive ACK/NAKs")
    sys.exit(-1)

# This function should not need any changes
def parse_args():
    if len(sys.argv) != 9:
        print_usage()

    is_server = False
    mode = "GARBAGE"
    remote_host = ""

    if sys.argv[1] == "SW":
        mode = "SW"
    elif sys.argv[1] == "GBN":
        mode = "GBN"
    else:
        print_usage()

    if sys.argv[8] == "server":
        is_server = True
    elif sys.argv[8] == "client":
        is_server = False
    else:
        print_usage()

    server_port = int(sys.argv[2])
    client_port = int(sys.argv[3])

    num_messages = int(sys.argv[4])
    N = int(sys.argv[5])
    isn = int(sys.argv[6])

    remote_host = sys.argv[7]

    return is_server, mode, server_port, client_port, num_messages, N, isn, remote_host


# This function will need to be adjusted if you change client() or server()'s prototypes
def main():
    # Try arg parsing from the command line
    (is_server, mode, server_port, client_port, num_messages, N, isn, remote_host) = parse_args()
    if mode == "GBN":
        gbn = True
    else:
        gbn = False

    # If there is a knownhosts file we are on Submitty, extract the port numbers
    if os.path.isfile("knownhosts_udp.txt"):
        print("Detected a knownhosts file, parsing", flush=True)
        with open("knownhosts_udp.txt") as knownfile:
            knownhosts = knownfile.readlines()
            for line in knownhosts:
                print("read knownhosts line: " + line, flush=True)
                line = line.split()
                if line[0] == "server":
                    server_port = int(line[1])
                if line[0] == "client":
                    client_port = int(line[1])

    # Launch ourselves in server/client mode
    if is_server:
        print("Starting in server mode", flush=True)
        server(gbn, server_port, client_port, remote_host, num_messages, N, isn)
    else:
        print("Starting in client mode, attempting to connect to {} on port {}".format(remote_host, server_port),
              flush=True)
        client(gbn, server_port, client_port, num_messages, N, isn, remote_host)

    sys.exit(0)


# Just make sure we're being invoked and not imported...
if __name__ == "__main__":
    main()