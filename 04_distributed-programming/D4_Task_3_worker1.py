import Pyro4
import math

@Pyro4.expose
class Worker1:
    def factorial(self, n):
        print(f"Worker1 calculating factorial({n})")
        return math.factorial(n)

# Start Pyro daemon
daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

uri = daemon.register(Worker1)
ns.register("worker1.service", uri)

print("Worker1 ready.")
daemon.requestLoop()