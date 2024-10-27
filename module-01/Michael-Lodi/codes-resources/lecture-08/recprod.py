def prod(S):
    res=1
    for e in S:
        res *=e
    return res

def prod_z(S):
    res=1
    for e in S:
        if e==0:
            return 0
        res *= e
    return res


def recprod(S):
    if len(S)==0:
        return 1
    else:
        return S[0]*recprod(S[1:])

class Zero(Exception):
    pass

def recprod(S):
    def aux(S):
        if len(S)==0:
            return 1
        else:
            if S[0]==0:
                raise Zero
            else:
                return S[0]*recprod(S[1:])
    try:
        res=aux(S)
    except Zero:
        return 0
    else:
        return res

def recp(S):
    if len(S)==0:
        return 1
    elif S[0]==0:
        return 0
    return S[0]*recp(S[1:])

def recp2(S):
    if len(S)==0:
        return 1
    elif S[0]==0:
        raise Zero
    try:
        return S[0]*recp2(S[1:])
    except Zero:
        return 0

T=(1,2,3,4,0,5,6,7,8,9,10)