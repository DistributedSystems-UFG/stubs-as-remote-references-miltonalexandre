from socket import *  # -
from time import sleep  # -
from random import *  # -
from constRPC import *  # -

# -
from client import *  # -
from server import *
from dbclient import *  # -


def client2():
    c2 = Client(PORTC2)  # create a new client
    data = c2.recvAny()  # block until data is sent
    dbC2 = pickle.loads(data)  # receive reference
    dbC2.appendData("Client 2")  # append data to same list
    print(dbC2.getValue())  # -
    c2.sendTo(HOSTS, PORTS, [STOP])  # -


if __name__ == "__main__":  # -
    client2()
