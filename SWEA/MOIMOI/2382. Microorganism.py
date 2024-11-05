from collections import defaultdict


# 이동 시키기
def move(i, j, num, dir):
    new_i, new_j = i + dir_info[dir][0], j + dir_info[dir][1]
    new_num = num
    new_dir = dir
    # 끝 점에 있을 때 방향 전환 후 미생물 반토막
    if new_i == 0 or new_j == 0 or new_i == N-1 or new_j == N-1:
        new_dir = dir_info[dir][2]
        new_num = num//2
    # 갱신된 정보 반환
    return (new_i, new_j, new_num, new_dir)


# 새로 만들어진 정보를 토대로 방향설정, 미생물 수 계산
def calculate(lst):
    lst.sort(key=lambda x:x[0], reverse=True)
    new_dir = lst[0][1]
    new_num = 0
    for num, dir in lst:
        new_num += num
    return [(new_num, new_dir)]


# 방향 좌표 설정 {방향 : X, Y, 벽을 만났을 때 다음 방향}
dir_info = {
    1: (-1, 0, 2),
    2: ( 1, 0, 1),
    3: (0, -1, 4),
    4: (0,  1, 3),
}

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    info = defaultdict(list)
    for k in range(K):
        i, j, num, dir = map(int, input().split())
        info[(i, j)].append((num, dir))

    for m in range(M):
        new_info = defaultdict(list)
        # 기존 딕셔너리 돌면서 이동 시키고 새로운 딕셔너리에 넣어주기
        for key, value in info.items():
            i, j = key
            now = value[0]
            num, dir = now
            # print(f'현재 좌표{i, j}')
            # print(f'현재 정보{num, dir}')
            ni, nj, nnum, ndir = move(i, j, num, dir)
            # print(ni, nj, num, ndir)
            new_info[(ni, nj)].append((nnum, ndir))
        
        # 새로운 딕셔너리 돌면서 계산 해주기
        for key, value in new_info.items():
            new_value = calculate(value)
            new_info[key] = new_value
        # 딕셔너리 바꿔치기
        info = new_info

    ans = 0

    for key, value in info.items():
        ans += value[0][0]
    print(f'#{tc} {ans}')
