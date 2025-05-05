# import Pyro4

# @Pyro4.expose
# class concatenate:
#     def concat(self , str1 , str2):
#         return str1 + str2
    

# daemon = Pyro4.Daemon()
# uri = daemon.register(concatenate)
# print(uri)

# daemon.requestLoop()

import Pyro4

@Pyro4.expose
class concatenate:
    def concat(self , str1 , str2):
        return str1 + str2
    

daemon = Pyro4.Daemon()
uri = daemon.register(concatenate)
print(uri)
daemon.requestLoop()
        