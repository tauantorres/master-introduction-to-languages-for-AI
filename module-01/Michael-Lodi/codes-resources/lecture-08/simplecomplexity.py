def summ(S):
    res=0
    for i in S:
        res+=i
    return res

def f(S):
    for e in S:
        if e==summ(S):
            return 'OK'
    return 'KO'
'''
for body: len(S)
for evaluated len(S) times
TOTAL time needed for f: len(S)**2 + 1
'''

def g(S):
    savesum=summ(S)
    for e in S:
        if e==savesum:
            return 'OK'
    return 'KO'
'''
for body: 1
for evaluated len(S) times
savesum=summ(S): len(S)
final return: 1
TOTAL len(S)+len(S) +1: linear