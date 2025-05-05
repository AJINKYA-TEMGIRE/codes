# import Pyro4

# uri = input("Enter the uri")

# server = Pyro4.Proxy(uri)
# result = server.concat("aj" , "ga")

# print(result)

import Pyro4

uri = input("Enter the uri: ")

server = Pyro4.Proxy(uri)
result = server.concat("aj" , "ga")
print(result)