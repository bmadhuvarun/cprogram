
g={'5':['4','3'],'4':['1','2'],'3':[],'1':[],'2':[]}

v=set()
def dfs(g,v,n):
    if n not in v:
        print(n)
        v.add(n)
        for ne in g[n]:
            dfs(g,v,ne)
print("path")
dfs(g,v,'5')
            
