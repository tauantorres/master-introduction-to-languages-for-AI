class Exitloop(Exception): pass
try:
    while True:
        while True:
            for i in range(10):
                if i > 3:
                    raise Exitloop  # break would exit just one level
                print("loop3: ", i)
            print("loop2")
        print("loop1")
except Exitloop:
    print('caught')
