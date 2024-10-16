# 10월 16일
# 과제는 끝나지 않아!
import sys
input = sys.stdin.readline

N = int(input())
my_work = []
point = 0
for _ in range(N):
    info = list(map(int, input().split()))
    if info[0] == 0:
        if my_work:
            my_work[-1][2] -=1
            if my_work[-1][2] == 0:
                point += my_work[-1][1]
                my_work.pop()
        else:
            continue
    else:
        info[2] -= 1
        if info[2] == 0:
            point += info[1]
        else:
            my_work.append(info)
print(point)