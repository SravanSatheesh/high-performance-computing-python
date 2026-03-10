import Pyro4
import math

@Pyro4.expose
class Worker2:
    def factorial(self, n):
        print(f"Worker2 calculating factorial({n})")
        return math.factorial(n)

# Start Pyro daemon
daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

uri = daemon.register(Worker2)
ns.register("worker2.service", uri)

print("Worker2 ready.")
daemon.requestLoop()