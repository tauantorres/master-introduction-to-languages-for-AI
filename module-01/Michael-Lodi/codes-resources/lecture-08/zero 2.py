def zero(S):
    for e in S:
        if e==0:
            return 'Ok'
    return 'ko'
'''
size = len(S)
worst case: 0 not in S

for body: 1 elementary op
for body is evaluated len(S) times
final return: 1
TOTAL: len(S)+1 operations
'''