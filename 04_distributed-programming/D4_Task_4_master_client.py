import Pyro4
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- Logging setup ---
logging.basicConfig(
    filename="Task_4_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# --- Connect to workers ---
workers = [
    Pyro4.Proxy("PYRONAME:task4.worker1"),
    Pyro4.Proxy("PYRONAME:task4.worker2")
]

# --- List of tasks (10 numbers) ---
tasks = [5, 6, 4, 7, 3, 8, 2, 9, 10, 1]

# --- Function to send task to worker and log ---
def send_task(worker, task):
    worker_name = worker._pyroUri.object
    logging.info(f"Sending task {task} to {worker_name}")
    print(f"{worker_name} processing task {task}")
    result = worker.process_task(task)
    logging.info(f"Task {task} result: {result}")
    return (worker_name, task, result)

# --- Store results ---
results = []

# --- Dynamic task assignment using threads ---
with ThreadPoolExecutor(max_workers=len(workers)) as executor:
    future_to_worker_task = {}  # map future -> (worker_index, task_index)

    # Submit initial tasks (one per worker)
    for i in range(len(workers)):
        future = executor.submit(send_task, workers[i], tasks[i])
        future_to_worker_task[future] = (i, i)

    next_task_index = len(workers)  # index of next task to assign

    # Process futures dynamically
    while future_to_worker_task:
        for future in as_completed(future_to_worker_task):
            worker_index, task_index = future_to_worker_task[future]
            worker_name, task, result = future.result()
            results.append(result)

            # Assign next task dynamically if available
            if next_task_index < len(tasks):
                # Assign to the same worker that just became free
                future_new = executor.submit(send_task, workers[worker_index], tasks[next_task_index])
                future_to_worker_task[future_new] = (worker_index, next_task_index)
                next_task_index += 1

            # Remove completed future
            del future_to_worker_task[future]
            break  # re-evaluate as_completed

# --- Print final results ---
print("All tasks done.")
print("Results:", results)
logging.info("All tasks completed.")