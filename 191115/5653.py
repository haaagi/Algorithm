import sys
sys.stdin = open('input_5653.txt','r')


def chk(q, k):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while k > 0:
        xx = -1
        for _ in range(len(q)):
            xx += 1
            if q[xx][2] == -1 and q[xx][1] == 0:
                q.pop(xx)
                xx -= 1
        k -= 1
        for idx in range(len(q)):
            if q[idx][1] < q[idx][0] and q[idx][2] != -1:
                q[idx][2] = -1
                q[idx][1] -= 1
            elif q[idx][1] == q[idx][0] and q[idx][2] != -1:
                for p in range(4):
                    if 0 <= q[idx][3] + dx[p] <= 700 and 0 <= q[idx][4] + dy[p] <= 700 and not visited[q[idx][3] + dx[p]][q[idx][4] + dy[p]]:
                        pan[q[idx][3] + dx[p]][q[idx][4] + dy[p]] = [[q[idx][0], 2*q[idx][0], 0, q[idx][3] + dx[p], q[idx][4] + dy[p]]]
                        visited[q[idx][3] + dx[p]][q[idx][4] + dy[p]] = 1
                        q.append([q[idx][0], 2*q[idx][0], 0, q[idx][3] + dx[p], q[idx][4] + dy[p]])
                q[idx][1] -= 1
            else:
                q[idx][1] -= 1
        q.sort(reverse=True)
    return

T = int(input())

for tc in range(T):
    pan = [[0 for _ in range(701)]for _ in range(701)]
    visited = [[0 for _ in range(701)] for _ in range(701)]

    n, m ,k = map(int, input().split())

    temp = [list(map(int, input().split())) for _ in range(n)]
    q = []
    for i in range(n):
        for j in range(m):
            if temp[i][j] > 0:
                # temp 는 라이프 사이클, 지금 현재 남은 생명력, 활성 비활성화 죽음(1, 0, -1) 상태
                pan[701//2-n//2+i][701//2-m//2+j] = [temp[i][j], 2*temp[i][j], 0, 701//2-n//2+i, 701//2-m//2+j]
                q.append([temp[i][j], 2*temp[i][j], 0, 701//2-n//2+i, 701//2-m//2+j])
                visited[701//2-n//2+i][701//2-m//2+j] = 1
    q.sort(reverse=True)
    chk(q, k)
    result = 0
    for cnt in q:
        if cnt[1] > 0:
            result += 1
    print('#{} {}'.format(tc+1, result))



