import Pyro4

@Pyro4.expose
class Fibonacci:
    
    def calculate(self, n):
        if n <= 1:
            return n
        return self.calculate(n-1) + self.calculate(n-2)
    
        # prime no calculation
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

# start Pyro Daemon
daemon = Pyro4.Daemon()  # create Pyro Server-Daemon
ns = Pyro4.locateNS()    # search name server
uri = daemon.register(Fibonacci)  # register server object
ns.register("fibonacci.service", uri)  # register an object in the name server under a name.

print("Fibonacci-Service gestartet.")
print("URI:", uri)

# run the server in an infinite loop.
daemon.requestLoop()
