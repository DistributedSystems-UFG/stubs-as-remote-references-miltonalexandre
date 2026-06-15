from socket import *  # -
from time import sleep  # -
from random import *  # -
from constRPC import *  # -

# -
from client import *  # -
from server import *
from dbclient import *  # -


# -
def client1():
    c1 = Client(PORTC1)  # create client
    dbC1 = DBClient(HOSTS, PORTS)  # create reference
    dbC1.create()  # create new list
    dbC1.appendData("Client 1")  # append some data
    c1.sendTo(HOSTC2, PORTC2, dbC1)  # send to other client


if __name__ == "__main__":
    client1()

