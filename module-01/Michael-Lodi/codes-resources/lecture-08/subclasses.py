class MyExcp(Exception): pass 
class MySpecific1(MyExcp): pass 
class MySpecific2(MyExcp): pass 

for e in (MyExcp(0), MySpecific1(1), MySpecific2(2)):
    try:
        raise e
    except MyExcp as X:
        print('caught ', X)
