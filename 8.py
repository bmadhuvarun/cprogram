def funcol(g):
    colors={}
    avacol={'red','yellow','green'}
    for vertice in g:
        used=set(colors[neg] for neg in g[vertice] if neg in colors)
        for color in avacol:
            if color not in used:
                break
        colors[vertice]=color
    return colors


if __name__=="__main__":
    g={
        'a':['b','c'],
        'b':['c','a'],
        'c':['a','b']
    }
    result=funcol(g)
    print("vertice color")
    for vertice,color in result.items():
        print(vertice ,color)
