# def supernova(n, ln, lm, rev):
#     global ans
#
#     if ans == 1:
#         return
#
#
#     if (n, rev) in check:
#         return
#
#     check.add((n, rev))
#
#     if ln == lm:
#         if rev == 1:
#             if n[::-1] == M:
#                 ans = 1
#                 return
#             else:
#                 return
#         else:
#             if n == M:
#                 ans = 1
#                 return
#             else:
#                 return
#
#     if ln >= lm:
#         return
#     # A추가
#     if rev == 0:
#         supernova(n + "A", ln + 1, lm, rev)
#     else:
#         supernova("A" + n, ln + 1, lm, rev)
#     # B 추가
#     if rev == 0:
#         supernova((n + "B"), ln + 1, lm, 1)
#     else:
#         supernova(("B" + n), ln + 1, lm, 0)
#
# N = input()
# M = input()
# ans = 0
# ln = len(N)
# lm = len(M)
# check = set()
# supernova(N, ln, lm, 0)
# print(ans)

# def solve(target, s):
#     if len(target) == len(s):
#         return 1 if target == s else 0
#
#     if len(target) < len(s):
#         return 0
#
#     result = 0
#
#     # 마지막 문자가 A인 경우
#     if target[-1] == 'A':
#         result = max(result, solve(target[:-1], s))
#
#     # 마지막 문자가 B인 경우
#     if target[0] == 'B':
#         result = max(result, solve(target[1:][::-1], s))
#
#     return result
#
#
# S = input()
# T = input()
# print(solve(T, S))

