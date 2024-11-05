# 큐빙

# 명령 읽어서 어떤 것을 움직일지 판단하는 햄수

def check(face):
    global top, bottom, front, back, left, right
    if face == 'U':
        new_top = [[''] * cube_range for _ in range(cube_range)]
        for i in range(cube_range):
            for j in range(cube_range):
                new_top[j][cube_range - 1 - i] = top[i][j]
        top = new_top
        front[0][0], front[0][1], front[0][2], right[0][0], right[0][1], right[0][2], back[0][0], back[0][1], back[0][2], left[0][0], left[0][1], left[0][2] = right[0][0], right[0][1], right[0][2], back[0][0], back[0][1], back[0][2], left[0][0], left[0][1], left[0][2], front[0][0], front[0][1], front[0][2]

    elif face == 'D':
        new_bottom = [[''] * cube_range for _ in range(cube_range)]
        for i in range(cube_range):
            for j in range(cube_range):
                new_bottom[j][cube_range - 1 - i] = bottom[i][j]
        bottom = new_bottom
        # front[2][2], front[2][1], front[2][0], left[2][2], left[2][1], left[2][0], back[2][2], back[2][1], back[2][0], right[2][2], right[2][1], right[2][0] = right[2][2], right[2][1], right[2][0], front[2][2], front[2][1], front[2][0], left[2][2], left[2][1], left[2][0], back[2][2], back[2][1], back[2][0]
        front[2][0], front[2][1], front[2][2], left[2][0], left[2][1], left[2][2], back[2][0], back[2][1], back[2][2], right[2][0], right[2][1], right[2][2] = left[2][0], left[2][1], left[2][2], back[2][0], back[2][1], back[2][2], right[2][0], right[2][1], right[2][2], front[2][0], front[2][1], front[2][2]

    elif face == 'F':
        new_front = [[''] * cube_range for _ in range(cube_range)]
        for i in range(cube_range):
            for j in range(cube_range):
                new_front[j][cube_range - 1 - i] = front[i][j]
        front = new_front
        bottom[0][0], bottom[0][1], bottom[0][2], right[2][0], right[1][0], right[0][0], top[2][2], top[2][1], top[2][0], left[0][2], left[1][2], left[2][2] = right[2][0], right[1][0], right[0][0], top[2][2], top[2][1], top[2][0], left[0][2], left[1][2], left[2][2], bottom[0][0], bottom[0][1], bottom[0][2]

    elif face == 'B':
        new_back = [[''] * cube_range for _ in range(cube_range)]
        for i in range(cube_range):
            for j in range(cube_range):
                new_back[j][cube_range - 1 - i] = back[i][j]
        back = new_back
        bottom[2][2], bottom[2][1], bottom[2][0], left[2][0], left[1][0], left[0][0], top[0][0], top[0][1], top[0][2], right[0][2], right[1][2], right[2][2] = left[2][0], left[1][0], left[0][0], top[0][0], top[0][1], top[0][2], right[0][2], right[1][2], right[2][2], bottom[2][2], bottom[2][1], bottom[2][0]

    elif face == 'L':
        new_left = [[''] * cube_range for _ in range(cube_range)]
        for i in range(cube_range):
            for j in range(cube_range):
                new_left[j][cube_range - 1 - i] = left[i][j]
        left = new_left
        bottom[2][0], bottom[1][0], bottom[0][0], front[2][0], front[1][0], front[0][0], top[2][0], top[1][0], top[0][0], back[0][2], back[1][2], back[2][2] = front[2][0], front[1][0], front[0][0], top[2][0], top[1][0], top[0][0], back[0][2], back[1][2], back[2][2], bottom[2][0], bottom[1][0], bottom[0][0]


    elif face == 'R':
        new_right = [[''] * cube_range for _ in range(cube_range)]
        for i in range(cube_range):
            for j in range(cube_range):
                new_right[j][cube_range - 1 - i] = right[i][j]
        right = new_right
        bottom[0][2], bottom[1][2], bottom[2][2], back[2][0], back[1][0], back[0][0], top[0][2], top[1][2], top[2][2], front[0][2], front[1][2], front[2][2] = back[2][0], back[1][0], back[0][0], top[0][2], top[1][2], top[2][2], front[0][2], front[1][2], front[2][2], bottom[0][2], bottom[1][2], bottom[2][2]
    else:
        print('!!!!!!!')

cube_range = 3
test_case = int(input())
for _ in range(test_case):
    N = int(input())
    # 윗면
    top = [
        ['w', 'w', 'w'],
        ['w', 'w', 'w'],
        ['w', 'w', 'w']
   ]
    bottom =[
        ['y', 'y', 'y'],
        ['y', 'y', 'y'],
        ['y', 'y', 'y']
    ]
    front = [
        ['r', 'r', 'r'],
        ['r', 'r', 'r'],
        ['r', 'r', 'r']
    ]
    back = [
        ['o', 'o', 'o'],
        ['o', 'o', 'o'],
        ['o', 'o', 'o']
    ]
    left = [
        ['g', 'g', 'g'],
        ['g', 'g', 'g'],
        ['g', 'g', 'g']
    ]
    right = [
        ['b', 'b', 'b'],
        ['b', 'b', 'b'],
        ['b', 'b', 'b']
    ]



    info = list(input().split())
    for i in info:
        if i[1] == '-':
            for _ in range(3):
                check(i[0])

        elif i[1] == '+':
            check(i[0])

    for i in range(cube_range):
        for j in range(cube_range):
            print(top[i][j], end='')
        print()