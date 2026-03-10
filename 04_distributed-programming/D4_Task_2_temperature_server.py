import Pyro4

# 1️⃣ Define the server class as instructed
@Pyro4.expose
class TemperatureConverter:
    
    # Convert Celsius to Fahrenheit
    def to_fahrenheit(self, celsius):
        return celsius * 9/5 + 32

    # Convert Fahrenheit to Celsius
    def to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

# 2️⃣ Start Pyro daemon and register the object
daemon = Pyro4.Daemon()             # Start Pyro server daemon
ns = Pyro4.locateNS()               # Locate the Pyro name server

# Register the class object in Pyro and give it a network name
uri = daemon.register(TemperatureConverter)
ns.register("temperature.service", uri)

print("Temperature service started.")
print("URI:", uri)

# 3️⃣ Run server in infinite loop
daemon.requestLoop()