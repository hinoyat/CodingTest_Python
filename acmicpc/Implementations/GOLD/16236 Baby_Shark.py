# 아기 상어
from collections import deque


def shark_move(si, sj):
    shark = 2
    shark_eat = 0
    time = 0
    # print(si, sj)
    while True:
        t, si, sj = find_fish(si, sj, shark)
        # print(si, sj, t)
        if t == -1:
            break
        shark_eat += 1
        time += t
        if shark_eat == shark:
            shark_eat = 0
            shark += 1
        sea[si][sj] = 0

    return time


def find_fish(i, j, shark):
    # bfs 돌리면 어차피 가까운 곳을 간다 shark move에서 while로 반복
    # 동거리 많다면 정렬해서 처리
    visited = [[0] * N for _ in range(N)]
    eat_list = []
    que = deque()
    que.append((0, i, j))
    visited[i][j] = 0

    while que:
        # print(1)
        t, qi, qj = que.popleft()
        for ni, nj in ((qi - 1, qj), (qi, qj - 1), (qi + 1, qj), (qi, qj + 1)):
            if 0<= ni< N and 0 <= nj < N and not visited[ni][nj]:
                if sea[ni][nj] <= shark:
                    visited[ni][nj] = visited[qi][qj] + 1
                    que.append((visited[ni][nj], ni, nj))
                    if sea[ni][nj] > 0 and sea[ni][nj] < shark:
                        eat_list.append((visited[ni][nj], ni, nj))

    # print(eat_list)
    if not eat_list:
        return (-1, -1, -1)
    else:
        eat_list.sort(key = lambda x : (x[0], x[1], x[2]))
        return eat_list[0]



# 입력 받기 N 배열 크기, N X N 크기의 배열
N = int(input())

sea = [list(map(int,input().split())) for _ in range(N)]


# 시작 지점
shark_point = []
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark_point = [i, j]
            sea[i][j] = 0
            break

print(shark_move(shark_point[0], shark_point[1]))

# 조건

'''
# 이동
1. 크기 크면 못 지나가
2. 같으면 지나가기는 가능
3. 작으면 먹어 -> 0으로 만들기
'''
'''
 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다
더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
'''

