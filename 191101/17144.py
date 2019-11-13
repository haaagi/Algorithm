import sys
sys.stdin = open('input.txt','r')

r, c ,t = map(int, input().split())

pan = [list(map(int, input().split())) for _ in range(r)]

print(pan)