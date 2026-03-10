import multiprocessing

def increment_counter(counter, lock):
    for _ in range(1000000):
        with lock:
            counter.value += 1

if __name__ == "__main__":
    shared_counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    process1 = multiprocessing.Process(target=increment_counter, args=(shared_counter, lock))
    process2 = multiprocessing.Process(target=increment_counter, args=(shared_counter, lock))

    process1.start()
    process2.start()
    process1.join()
    process2.join()

    print("Final Counter Value:", shared_counter.value)