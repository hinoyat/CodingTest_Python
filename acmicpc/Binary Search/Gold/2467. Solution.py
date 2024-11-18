N = int(input())
lst = list(map(int, input().split()))

lst.sort()

start = 0
end = N - 1

min_v = 21e8

start_bool = False
end_bool = False

acid = -1
alkali = -1


while start < end:
    temp_val = abs(lst[start] + lst[end])
    if temp_val < min_v:
        min_v = temp_val
        acid = lst[start]
        alkali = lst[end]

    if abs(lst[start + 1] + lst[end]) < abs(lst[start] + lst[end - 1]):
        start += 1
    else:
        end -= 1
print(acid, alkali)
