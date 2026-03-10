import Pyro4
import math
import time

@Pyro4.expose
class Worker:
    def process_task(self, n):
        print(f"Worker1 processing task {n}")
        time.sleep(2)  # simulate work
        result = math.factorial(n)
        print(f"Worker1 finished task {n}")
        return result

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(Worker)
ns.register("task4.worker1", uri)

print("Task 4 Worker1 ready.")
daemon.requestLoop()