
import zmq

#test2
context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def request(toop):
    toop_bytes =  str(toop).encode()
    #print(toop_bytes)

    socket.send(toop_bytes)

    #  Get the reply.
    message = socket.recv()
    decoded = message.decode()
    #print("Received reply %s [ %s ]" % (toop_bytes, decoded))
    return decoded
print(request((1,"BOTW")))