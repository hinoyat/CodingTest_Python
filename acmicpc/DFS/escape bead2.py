from pprint import pprint
N, M = map(int, input().split())

#  조건
'''
// 이건 종료
1. 파란 구슬 구멍에 들어감
2. 동시에 빠져도 실패
3. 구슬이 움직이지 않을 때 까지 움직이기

// 이건 주의사항
1. 동시 같은 칸 X
2. 한 칸을 모두 차지
# 벽
. 통로
O 구멍
R 빨강
B 파랑

// 필요한 함수
1. 공의 움직임 구현
 - 두 공이 모두 움직이지 않을 때 까지
2. 백트래킹 - 이전의 움직임과 반대 방향을 안 해야 하지 않을까?
'''

def move_ball():
    pass

def supernova():
    pass



Game_Board = [list(input()) for _ in range(N)]
pprint(Game_Board)
ans = 1998