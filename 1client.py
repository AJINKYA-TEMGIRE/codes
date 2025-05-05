# import xmlrpc.client


# server = xmlrpc.client.ServerProxy("http://localhost:8000")
# result = server.fact(5)

# print(result)


import xmlrpc.client

n = int(input("Enter the number: "))

server = xmlrpc.client.ServerProxy("http://localhost:8000")
result = server.calculate(n)
print(result)

