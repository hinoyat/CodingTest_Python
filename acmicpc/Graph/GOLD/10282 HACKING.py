import heapq
import sys
input = sys.stdin.readline
def hacking(start):
    computer = []
    visited = [21e8] * (N + 1)
    heapq.heappush(computer, (0, start))
    visited[start] = 0

    while computer:
        qtime, qnum = heapq.heappop(computer)
        for ntime, nnum in PC[qnum]:
            new_time = qtime + ntime
            if new_time < visited[nnum]:
                visited[nnum] = new_time
                heapq.heappush(computer, (new_time, nnum))

    return visited

T = int(input())
# 일방통행
for tc in range(1, T+1):

    N, D, C = map(int, input().split())

    PC = [[] for _ in range(N + 1)]
    for _ in range(D):
        A, B, time = map(int, input().split())
        PC[B].append((time, A))
    # print(PC)

    result = hacking(C)
    # print(result)
    cnt = 0
    max_time = 0

    for r in result:
        if r != 21e8:
            cnt += 1
            max_time = max(max_time, r)

    print(cnt, max_time)