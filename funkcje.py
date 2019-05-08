def czynnikiPierwsze(x):
    ret = []
    k=2
    while x>1:
        while x%k == 0:
            ret.append(k)
            x/=k
        k+=1
    return ret

def liczbaIWykladnik(list):
    if len(set(list)) == 1:
        return [list[0], len(list)]