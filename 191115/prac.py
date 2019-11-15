

def perm(arr, depth):
    if depth == 4:
        print(arr)
    over = 0
    for i in range(4):
        if not visited[i] and over != a[i]:
            visited[i] = 1
            arr.append(a[i])
            over = a[i]
            perm(arr, depth + 1)
            arr.pop()
            visited[i] = 0



a = [1,1,3,4]
visited = [0] * 4
arr = []
perm(arr, 0)
