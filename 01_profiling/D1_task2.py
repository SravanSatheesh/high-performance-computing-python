# extension.py

import time


# --- Task 1 functions (kept for timing demonstration) ---

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def do_stuff():
    result = []
    for i in range(0, 1_000_000):
        result.append(i * i)
    return result


def waste_time():
    time.sleep(5)
    print("Finished wasting time.")


# --- Task 2: Measure execution time ---

def main():
    # 1. store start time
    start = time.time()

    # program work
    print("Factorial of 5:", fact(5))
    squares = do_stuff()
    print("Generated", len(squares), "square values.")
    waste_time()

    # 2. store end time
    end = time.time()

    # 3. print execution duration
    print("\nExecution time:", end - start, "seconds")


# run program
if __name__ == "__main__":
    main()