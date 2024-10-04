# 알고리즘수업 - 병합정렬1
def merge_sort(p, r):
    if p < r:
        q = int((p+r)/2)
        merge_sort(p, q)
        merge_sort(q+1, r)
        merge(p, q, r)

def merge(p, q, r):
    result = []
    left = p
    right = q + 1

    while left <= q and right <= r:
        if lst[left] <= lst[right]:
            result.append(lst[left])
            ans.append(lst[left])
            left += 1
        else:
            result.append(lst[right])
            ans.append(lst[right])
            right += 1
    while left <= q:
        result.append(lst[left])
        ans.append(lst[left])
        left += 1
    while right <= r:
        result.append(lst[right])
        ans.append(lst[right])
        right += 1
    for i in range(len(result)):
        lst[p + i] = result[i]

ans = []
cnt = 0

N, M = map(int, input().split())
lst = list(map(int, input().split()))
result = merge_sort(0, N-1)

if len(ans) < M:
    print(-1)
else:
    print(ans[M - 1])