import time

def slow_function():
    print("Rozpoczynam dziakanie slow_function...")
    time.sleep(3) #program stoi przez 3 sekundy
    print("Zakonczylem dzialanie slow_function")

print("Zaczynam pomiar czasu")
start_time = time.time() # znacznik czasu w  momencie rozpoczecia dzialania pomiaru

slow_function()

end_time = time.time() # znacznik czasu w momencie zakonczenia dzialania pomiaru

elapsed_time = end_time - start_time # roznica czasu

print(f"Funkcja wykonala sie w czasie {elapsed_time} sekund")