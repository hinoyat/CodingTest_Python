from collections import deque
import sys

input = sys.stdin.readline
def bfs() :
    q = deque()
    q.append([0,0,K])
    visited[0][0][K] = 1
    while q :
        qi,qj,wall = q.popleft()
        if qi == N-1 and qj == M-1 :
            return visited[qi][qj][wall]
        for i in range(4) :
            ni ,nj = dx[i] + qi, dy[i]+qj
            if 0<=ni<N and 0<=nj<M :
                if arr[ni][nj]==1 and wall>0 and visited[ni][nj][wall-1]==0:
                    visited[ni][nj][wall-1] = visited[qi][qj][wall]+1
                    q.append([ni,nj,wall-1])


                    
                elif arr[ni][nj]==0 and visited[ni][nj][wall]==0:
                    visited[ni][nj][wall] = visited[qi][qj][wall]+1
                    q.append([ni,nj,wall])
    return -1


N,M,K = map(int, input().split())
visited = [[[0]*(K+1) for _ in range(M)] for __ in range(N)]
arr = [list(map(int,input().strip())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]


print(bfs())