def is_safe(b,r,c):
    return all(b[i]!=c and abs(b[i]-c)!=r-i for i in range(r))
def chess(n,b=[],r=0):
    if(n==r):
        return [b[:]]
    s=[]
    for c in range(n):
        if is_safe(b,r,c):
            s.extend(chess(n,b+[c],r+1))
    return s
print(chess(3))
