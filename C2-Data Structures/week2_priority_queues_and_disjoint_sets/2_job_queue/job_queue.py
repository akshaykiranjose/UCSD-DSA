# python3

from collections import namedtuple
AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

p_idx = lambda x: max(0, (x-1)//2)

def violation(data, i):
    """Is the heap property violated at index (idx) of heap (data)
    """
    n = len(data)
    left = 2*i+1
    right = 2*i+2

    """For the worker-task, accomodate the tie-breaker
       tuple of (priority, tie_index) """
    def is_less(a, b):
        # Returns True if a should come before b in the heap
        if a[0] < b[0]:
            return True
        elif a[0] == b[0]:
            return a[1] < b[1]
        return False
    
    swap_idx = i
    if left < n and is_less(data[left], data[swap_idx]):
        swap_idx = left

    if right < n and is_less(data[right], data[swap_idx]):
        swap_idx = right

    return swap_idx if swap_idx != i else -1

    
def sift_down(data, idx):
    while True:
        swap_idx = violation(data, idx)
        if swap_idx == -1:
            break
        data[idx], data[swap_idx] = data[swap_idx], data[idx]
        idx = swap_idx

def sift_up(data, idx):
    while True:
        # check for parent violating the heap property
        idx = p_idx(idx)
        swap_idx = violation(data, idx)
        if swap_idx == -1:
            break
        #make sure idx and swap_idx don't have the same value
        data[idx], data[swap_idx] = data[swap_idx], data[idx]

class Heap:
    def __init__(self, data):
        self.size = len(data)
        self.data = data
        for i in range(self.size//2, -1, -1):
            sift_down(self.data, i)

    def insert(self, item):
        self.data.append(item)
        self.size += 1
        sift_up(self.data, self.size-1)

    def extract(self):
        item = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop(-1)
        if self.data:
            self.size -= 1
            sift_down(self.data, 0)
        return item


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    # next_free_time = [0] * n_workers
    # for job in jobs:
    #     next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
    #     result.append(AssignedJob(next_worker, next_free_time[next_worker]))
    #     next_free_time[next_worker] += job
    worker_q = Heap([(0, i) for i in range(n_workers)])
    
    for job_t in jobs:
        free_at, worker = worker_q.extract()
        result.append(AssignedJob(worker, free_at))
        worker_q.insert((free_at + job_t, worker))
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
