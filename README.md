# Microservice Server

Microservice Server is a Python random number generator.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install zmq

```

pip install zmq

```

## Usage

Use ZeroMQ sockets to connect to the socket at ("tcp://localhost:5555")

To use the server properly, send to the socket an encoded tuple with a 1 or 2 as the first index of the tuple <br />
To REQUEST data connect to the socket using
```
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
```
then send
```
socket.send(message_as_a_tuple)
```
to RECEIVE data after connecting to the socket, use
```
message = socket.recv()
decoded = message.decode()
```

for example (1, 'string') could be used in this manner

```
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
```
<img width="684" alt="Screenshot 2024-02-25 at 5 08 35 PM" src="https://github.com/jpulattie/LoanAppCalculatorProject/assets/97932025/4da474a6-8984-4f27-af48-e3dbf1391288">


## License

[MIT](https://choosealicense.com/licenses/mit/)
