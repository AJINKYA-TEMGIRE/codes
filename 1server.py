# from xmlrpc.server import SimpleXMLRPCServer

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)


# server = SimpleXMLRPCServer(("localhost" , 8000)) 
# server.register_function(factorial , "fact")
# server.serve_forever()


from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


server = SimpleXMLRPCServer(("localhost" , 8000))
server.register_function(factorial , "calculate")
print("Server is Ready...")
server.serve_forever() 


