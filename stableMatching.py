   
def stableMatching(m, w):

    M = []
    F = []
    pairs = {}

    for i in range(len(m)):
        for f in m[i]:
            if f not in F:
                pairs[f] = i
                M.append(i)
                F.append(f)
            elif f in F:
                e = pairs[f]
                if w[f].index(i) > w[f].index(e):
                    pairs[f] = i
                    M.append(i)
                    M.remove(e)
                
    return print(pairs)
      
