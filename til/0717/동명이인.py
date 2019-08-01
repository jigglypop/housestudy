def F(m):
    N = {}
    for i in m:
        if i in N:
            N[i] += 1 
        else:
            N[i] = 1
    r = set()
    for i in N:
        if N[i] >= 2:
            r.add(i)        
    return r

n1 = ['a','b','c','a']
print(F(n1))
