from libs._bridge import init, submit, close
from collections import deque

NICKNAME = '적기지파괴전략'
game_data = init(NICKNAME)

# 상수 정의
DIRECTIONS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
ROTATIONS = {'U': 0, 'R': 1, 'D': 2, 'L': 3}

# 게임 상태 변수
map_data = []
allies = {}
enemies = {}
codes = []

def parse_data(game_data):
    global map_data, allies, enemies, codes
    lines = game_data.split('\n')
    
    map_height, map_width, num_allies, num_enemies, num_codes = map(int, lines[0].split())
    
    map_data = [list(line.split()) for line in lines[1:map_height+1]]
    
    allies = {parts[0]: parts[1:] for parts in (line.split() for line in lines[map_height+1:map_height+1+num_allies])}
    
    enemies = {parts[0]: parts[1:] for parts in (line.split() for line in lines[map_height+1+num_allies:map_height+1+num_allies+num_enemies])}
    
    codes = lines[map_height+1+num_allies+num_enemies:]

def find_unit(unit_char):
    return next(((i, j) for i, row in enumerate(map_data) 
                 for j, cell in enumerate(row) if cell == unit_char), None)

def bfs(start, target):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        (i, j), path = queue.popleft()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        
        if map_data[i][j] == target:
            return path
        
        for direction, (di, dj) in DIRECTIONS.items():
            ni, nj = i + di, j + dj
            if 0 <= ni < len(map_data) and 0 <= nj < len(map_data[0]) and map_data[ni][nj] not in ['R', 'F', 'W']:
                queue.append(((ni, nj), path + [direction]))
    return None

def get_next_move():
    my_pos = find_unit('A')
    enemy_base_pos = find_unit('X')
    
    if not enemy_base_pos:
        return "S"  # 적 기지가 없으면 대기
    
    path = bfs(my_pos, 'X')
    if not path:
        return "S"  # 경로가 없으면 대기
    
    next_pos = (my_pos[0] + DIRECTIONS[path[0]][0], my_pos[1] + DIRECTIONS[path[0]][1])
    
    # 적 기지 옆에 도달했는지 확인
    if map_data[next_pos[0]][next_pos[1]] == 'X':
        return f"{path[0]} F M"  # 일반 포탄으로 공격
    
    # 나무를 만나면 파괴
    if map_data[next_pos[0]][next_pos[1]] == 'T':
        return f"{path[0]} F M"
    
    # 그 외의 경우 전진
    return f"{path[0]} A"

def print_game_state():
    print("\n현재 게임 상태:")
    print("맵:")
    for row in map_data:
        print(' '.join(row))
    print("\n아군 정보:", allies)
    print("적군 정보:", enemies)
    print("암호문:", codes)

# 메인 게임 루프
while game_data is not None:
    parse_data(game_data)
    print_game_state()
    
    move = get_next_move()
    print(f"선택한 행동: {move}")
    
    game_data = submit(move)

close()