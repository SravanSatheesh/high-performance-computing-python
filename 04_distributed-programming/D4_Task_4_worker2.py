import Pyro4
import math
import time

@Pyro4.expose
class Worker:
    def process_task(self, n):
        print(f"Worker2 processing task {n}")
        time.sleep(2)  # simulate work
        result = math.factorial(n)
        print(f"Worker2 finished task {n}")
        return result

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(Worker)
ns.register("task4.worker2", uri)

print("Task 4 Worker2 ready.")
daemon.requestLoop()