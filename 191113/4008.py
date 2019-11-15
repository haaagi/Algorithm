import sys
sys.stdin = open('input_4008.txt','r')


def calc(arr):
    global mini, maxi
    num = numbers[0]
    idx = 1
    while idx <= len(numbers) -1:
        for i in range(len(arr)):
            if arr[i] == 1:
                num += numbers[idx]
                idx += 1
            elif arr[i] == 2:
                num -= numbers[idx]
                idx += 1
            elif arr[i] == 3:
                num = num * numbers[idx]
                idx += 1
            else:
                num = num // numbers[idx]
                idx += 1
    mini = min(mini, num)
    maxi = max(maxi, num)
    return


def perm(arr, depth):
    if depth == a:
        calc(arr)
    else:
        for i in range(a):
            if not visited[i]:
                visited[i] = 1
                perm(arr+[oper[i]], depth+1)
                visited[i] = 0


T = int(input())

for tc in range(T):
    n = int(input())
    # + - *  /
    opers = list(map(int,input().split()))
    numbers = list(map(int, input().split()))

    a = sum(opers)
    oper = [0] * a
    j = 0
    for i in range(4):
        if opers[i] >= 1:
            for x in range(opers[i]):
                oper[j] = i+1
                j += 1
    mini = 99999999
    maxi = 0
    visited = [0] * a
    perm([], 0)
    print('#{} {}'.format(tc+1, maxi-mini))





