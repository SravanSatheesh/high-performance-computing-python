import Pyro4

# Connect to workers
worker1 = Pyro4.Proxy("PYRONAME:worker1.service")
worker2 = Pyro4.Proxy("PYRONAME:worker2.service")

numbers = [4, 6, 3, 5]   # list of numbers to calculate
results = []

workers = [worker1, worker2]   # round-robin assignment

for i, num in enumerate(numbers):
    worker = workers[i % 2]    # alternate between worker1 and worker2
    result = worker.factorial(num)
    results.append(result)

print("Results:", results)