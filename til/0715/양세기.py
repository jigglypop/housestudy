# 5
# 1
# 2
# 11
# 1295
# 1692

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    
    
    
    Q = set([10000])
    c = 0
    
    while len(Q) < 11:
        c += 1
        m = c * n
        a = list(map(int,list(str(m))))
        b = set(a)
        Q = Q | b
        
    print(f'#{tc} {m}')


        

        
