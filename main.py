# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    jobs = [(t, i) for i, t in enumerate(data)]
    curr_jobs = {}

    for j in jobs:
        t, i = j
        thread_start, thread_id = heapq.heappop(threads)
        output.append((thread_id, thread_start))
        curr_jobs[thread_id] = i
        heapq.heappush(threads, (thread_start + t, thread_id))

    return output

def main():
    

    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for r in result:
        print(r[0], r[1])


if __name__ == "__main__":
    main()
