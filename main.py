import random
import time

def read_pressure():
    # Simulating tyre pressure between 25 and 40 PSI
    return round(random.uniform(25, 40), 2)

def check_pressure(pressure):
    if pressure < 30:
        print(f"⚠️ ALERT: Low Tyre Pressure - {pressure} PSI")
    else:
        print(f"✅ Pressure Normal - {pressure} PSI")

print("Tyre Pressure Monitoring System Started...\n")
while True:
    pressure = read_pressure()
    check_pressure(pressure)
    time.sleep(2)  # simulate sensor reading every 2 seconds
