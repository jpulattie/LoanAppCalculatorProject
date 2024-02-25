# Microservice Server

Microservice Server is a Python random number generator.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install zmq
''' 
pip install zmq
'''

## Usage

Use ZeroMQ sockets to connect to the socket at ("tcp://localhost:5555")

To use the server properly, send to the socket an encoded tuple with a 1 or 2 as the first index of the tuple

for example (1, 'string') could be used in this manner

'''
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def request(toop):
    toop_bytes =  str(toop).encode()
    socket.send(toop_bytes)
    message = socket.recv()
    decoded = message.decode()
    return decoded
print(request((1,"string")))
'''

## License

[MIT](https://choosealicense.com/licenses/mit/)
