import random


class Servers:
    def __init__(self , name):
        self.name = name
        self.connection = 0

class load:
    def __init__(self , servers):
        self.servers = servers

    def random(self):
        while True:
            yield random.choice(self.servers)

    def round(self):
        index = 0
        while True:
            yield self.servers[index]
            index = (index + 1) % len(self.servers)
        
    def min_conn(self):
        while True:
            min_conn = min(self.servers , key = lambda x : x.connection)
            min_conn.connection += 1
            yield min_conn

server1 = Servers("Server1")
server2 = Servers("Server2")
server3 = Servers("Server3")

lb = load(servers=[server1 , server2  ,server3 ]).min_conn()

for i in range(10):
    s = next(lb)
    print(s.name)