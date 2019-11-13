import sys
sys.stdin = open('input.txt','r')
n, m = map(int,input().split())

pan = [list(map(int, input())) for _ in range(n)]

visited = [[99999 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1
queue = []
x, y = 0, 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]  # 좌 우 상 하
queue.append((0,0))
while queue:
    x, y = queue.pop(0)
    for i in range(4):
        if 0 <= x + dx[i] <= n-1 and 0 <= y + dy[i] <= m-1:
            if pan[x+dx[i]][y+dy[i]] == 1 and visited[x][y] + 1 < visited[x + dx[i]][y + dy[i]]:
                queue.append((x + dx[i], y + dy[i]))
                visited[x + dx[i]][y + dy[i]] = visited[x][y] + 1


print('{}'.format(visited[n-1][m-1]))


