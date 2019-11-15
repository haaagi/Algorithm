import sys
sys.stdin = open('input_2117.txt','r')


def chk(cnt, k):
    global result
    if cost[k-1] <= cnt * m:
        return cnt
    else:
        return 0

def home(p, q):
    a = 0
    if 0 <= p <= n-1 and 0 <= q <= n-1:
        if pan[p][q] == 1:
            a += 1
    return a


def find(i, j, k):
    global result
    cnt = 0
    # 위쪽 좌우
    for x in range(1,k):
        for y in range(1, k-x):
            cnt += home(i-x, j-y)
            cnt += home(i-x, j+y)
        cnt += home(i-x, j)
    for x in range(1, k):
        cnt += home(i, j- x)
        cnt += home(i, j + x)
    cnt += home(i, j)
    for x in range(1,k):
        for y in range(1,k-x):
            cnt += home(i+x, j-y)
            cnt += home(i+x, j+y)
        cnt += home(i+x, j)

    result = max(result, chk(cnt, k))





T = int(input())

for tc in range(T):
    n, m = map(int,input().split())

    pan = [list(map(int, input().split()))for _ in range(n)]

    cost = [0] * (n+2)
    for i in range(1,n+2):
        cost[i-1] = (i-1)*(i-1) + i * i
    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(1,n+2):
                find(i,j,k)

    print('#{} {}'.format(tc+1, result))



