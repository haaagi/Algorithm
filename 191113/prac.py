def perm(arr, depth):
    if depth == 5:
        print(arr)
    else:
        for i in range(5):
            if not visited[i]:
                visited[i] = 1
                perm(arr+[a[i]], depth+1)
                visited[i] = 0

a = [1,2,3,4,4]
visited= [0] * 5
perm([], 0)
#
# def sol(depth, arr):
#     if depth == 4:
#         print(arr)
#     else:
#         for i in range(4):
#             if not visited[i]:
#                 visited[i] = True
#                 sol(depth+1, arr+[l[i]])
#                 visited[i] = False
# ​
# l = [1, 1, 3, 4]
# visited = [False]*4
# sol(0, [])