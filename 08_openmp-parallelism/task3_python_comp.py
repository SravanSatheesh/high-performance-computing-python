import time

N = 100_000_000
start = time.time()
total = sum(range(1, N+1))
end = time.time()

print("Python sum:", total)
print("Time:", end - start, "seconds")

# PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day8> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8/task3.py"
# Python sum: 5000000050000000
# Time: 1.547478437423706 seconds