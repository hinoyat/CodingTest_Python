from collections import deque

def find_minimum(now, target):
    que = deque()
    order = ''
    que.append((now, order))



T = int(input())

for _ in range(T):
    now, target = input().split()
