import multiprocessing
import time

def faulty_function(x):
    time.sleep(1)
    if x == 5:
        raise ValueError("Something went wrong with value 5")
    return x * x

def safe_worker(x):
    try:
        return ("result", faulty_function(x))
    except Exception as e:
        return ("error", str(e))

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]

    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(safe_worker, numbers)

    for msg_type, content in results:
        if msg_type == "result":
            print("Ergebnis:", content)
        else:
            print("Fehler:", content)