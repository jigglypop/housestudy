def D(sy,sx):
    m[sy][sx] = 0
    if sy == 0:
        return sx
    elif m[sy][sx-1] == 1:        
        return D(sy,sx-1)
    elif m[sy][sx+1] == 1:
        return D(sy,sx+1)
    else:
        return D(sy -1, sx)


sy,sx = -1,-1
T = int(input())
m = []
for i in range(100):
    b = list(map(int,input().split()))
    m.append([0]+b+[0])
m.append([0]*102) 
for y in range(101):
    for x in range(101):
        if m[y][x] == 2:
            sy,sx = y,x   
print(f'#{T} {D(sy,sx)-1}')