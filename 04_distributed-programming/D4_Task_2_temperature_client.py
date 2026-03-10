import Pyro4

# Connect to the remote service
converter = Pyro4.Proxy("PYRONAME:temperature.service")

# Test Celsius → Fahrenheit
celsius = 25
print(f"{celsius}°C in Fahrenheit:", converter.to_fahrenheit(celsius))

# Test Fahrenheit → Celsius
fahrenheit = 98.6
print(f"{fahrenheit}°F in Celsius:", converter.to_celsius(fahrenheit))