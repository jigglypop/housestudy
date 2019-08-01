T= int(input())
m = []
for tc in range(1, T+1):
	N, M = map(int, input().split())
	m += [list(map(int, input().split())) for _ in range(M)]
    print(m)