# 큐빙

# 명령 읽어서 어떤 것을 움직일지 판단하는 햄수

def check(face, way):
    global top, bottom, front, back, left, right

    if face == 'U':
        new_top = [[''] * cube_range for _ in range(cube_range)]
        for i in range(cube_range):
            for j in range(cube_range):
                new_top[i][j] = top[cube_range - 1 - i][j]
        top = new_top
        front[0][0], front[0][1], front[0][2], right[0][0], right[0][1], right[0][2], back[0][0], back[0][1], back[0][2], left[0][0], left[0][1], left[0][2] = right[0][0], right[0][1], right[0][2], back[0][0], back[0][1], back[0][2], left[0][0], left[0][1], left[0][2], front[0][0], front[0][1], front[0][2]

    elif face == 'D':
        new_bottom = [[''] * cube_range for _ in range(cube_range)]
        for i in range(cube_range):
            for j in range(cube_range):
                new_bottom[i][j] = bottom[cube_range - 1 - i][j]
        bottom = new_bottom
        front[2][0], front[2][1], front[2][2], right[2][0], right[2][1], right[2][2], back[2][0], back[2][1], back[2][2], left[2][0], left[2][1], left[2][2] = right[2][0], right[2][1], right[2][2], back[2][0], back[2][1], back[2][2], left[2][0], left[2][1], left[2][2], front[2][0], front[2][1], front[2][2]

    elif face == 'F':
        new_front = [[''] * cube_range for _ in range(cube_range)]
        for i in range(cube_range):
            for j in range(cube_range):
                new_front[i][j] = front[cube_range - 1 - i][j]
        front = new_front
        top[2][0], top[2][1], top[2][2], right[0][0], right[1][0], right[2][0], bottom[0]


    elif face == 'B':
        main_point = back
        sub_point = [top, bottom, left, right]

    elif face == 'L':
        main_point = left
        sub_point = [top, bottom, front, back]

    elif face == 'R':
        main_point = right
        sub_point = [top, bottom, front, back]




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
        i = i


arr = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
   ]

new_arr = [[0] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        new_arr[j][i] = arr[2- i][j]

print(new_arr)