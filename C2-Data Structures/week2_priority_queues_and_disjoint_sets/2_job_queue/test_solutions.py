import subprocess
import random
# Prepare the command and arguments
# Let's say the arguments are: 2 5 followed by 1 2 3 4 5

iter = 0
while True:
    iter += 1
    n_workers = random.randint(1, 5)
    n_jobs = random.randint(n_workers, 10)
    job_durations = [str(random.randint(1, 5)) for i in range(n_jobs)]
    user_input = f"{n_workers} {n_jobs}\n" + " ".join(job_durations) + "\n"

    # Run the script using subprocess
    result1 = subprocess.run(
        ["python", "2_job_queue/job_queue.py"],
        input=user_input,
        text=True,
        capture_output=True,
        timeout=6.00
    )

    try:
        result2 = subprocess.run(
            ["python", "2_job_queue/job_queue_1.py"],
            input=user_input,
            text=True,
            capture_output=True,
            timeout=6.00
        )
    except:
        print(user_input)
        print(result1.stdout)
        break

    if result1.stdout == result2.stdout:
        print(f"Iter: {iter}")
    else:
        print(user_input)
        print(result1.stdout)
        print(result2.stdout)
        break
