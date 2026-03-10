# extension.py

# a) Factorial function
def fact(n):
    """
    Calculate factorial of a given number n.
    Uses an iterative approach.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# b) Generate a list of square values
def do_stuff():
    """
    Generate square values from 0 to 999999
    and return them as a list.
    """
    result = []
    for i in range(0, 1_000_000):  # 0 .. 999999
        result.append(i * i)
    return result


# c) Wasting time
def waste_time():
    """
    Pause execution for 5 seconds, then print a message.
    """
    import time
    time.sleep(5)
    print("Finished wasting time.")


# d) Main program and function calls
def main():
    print("Factorial of 5:", fact(5))

    squares = do_stuff()
    print("Generated", len(squares), "square values.")

    waste_time()


if __name__ == "__main__":
    main()