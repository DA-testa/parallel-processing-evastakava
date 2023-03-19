# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    th = [(0, i) for i in range(n)]
    heapq.heapify(th)
    jobs = [(t, i) for i, t in enumerate(data)]
    c_jobs = {}

    for j in jobs:
        t, i = j
        th_start, th_id = heapq.heappop(th)
        output.append((th_id, th_start))
        c_jobs[th_id] = i
        heapq.heappush(th, (th_start + t, th_id))

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
