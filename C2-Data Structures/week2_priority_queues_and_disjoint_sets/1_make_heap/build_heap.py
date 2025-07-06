# python3

lc_idx = lambda idx: 2*idx + 1
rc_idx = lambda idx: 2*idx + 2

def violation(data, idx):
    """Is the heap property violated at index (idx) of heap (data)
    """
    lc = None if lc_idx(idx) >= len(data) else data[lc_idx(idx)]
    rc = None if rc_idx(idx) >= len(data) else data[rc_idx(idx)]
    
    if not lc and not rc:
        return 0
    
    if (lc and data[idx] > lc) and (rc and data[idx] > rc):
        return lc_idx(idx) if lc < rc else rc_idx(idx)
    elif (lc and data[idx] > lc):
        return lc_idx(idx)
    elif (rc and data[idx] > rc):
        return rc_idx(idx)
    else:
        return 0
    
def sift_down(data, idx, swaps):
    while True:
        swap_idx = violation(data, idx)
        if swap_idx == 0:
            break
        data[idx], data[swap_idx] = data[swap_idx], data[idx]
        swaps.append((idx, swap_idx))
        idx = swap_idx


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)//2, -1, -1):
        sift_down(data, i, swaps)
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    print(data)
    swaps = build_heap(data)
    print(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
