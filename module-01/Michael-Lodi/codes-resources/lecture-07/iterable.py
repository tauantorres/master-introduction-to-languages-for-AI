import random

class RandomIterable:
    def __iter__(self):
        return self
    def __next__(self):
        if random.choice(["go", "go", "stop"]) == "stop":
            raise StopIteration  # signals "the end"
        return 1

'''1/3: 0
2/3*1/3=2/9: 1
2/3*2/3*1/3=4/27: 2
2/3*2/3*2/3*1/3=8/81: 3
....
vedo k 1 con prob (2**k)/(3**(k+1))
'''

tentativi=100000
D={}
for i in range(tentativi):
    lun=0
    H=RandomIterable()
    for i in H:
        lun+=1
    D[lun]=D.get(lun,0)+1
for k in sorted(D.keys()):
    print(k, D[k], 'freq: ', D[k]/tentativi, 'prob: ', (2**k)/(3**(k+1)))
    
