import Pyro4

# Establish a connection with the server object.
fibonacci = Pyro4.Proxy("PYRONAME:fibonacci.service")

# Calling a remote methode
n = 10  # Example: Fibonacci of 10
result = fibonacci.calculate(n)
print(f"Fibonacci von {n} ist: {result}")
#prime check
print("Is 7 prime?", fibonacci.is_prime(7))
print("Is 10 prime?", fibonacci.is_prime(10))