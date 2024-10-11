import time 

def basicGen(n):
    yield n
    yield n + 1

def generator_with_list():
    arr = list('abcdefghijklmnopqrstuvwxyz')

    for x in range(len(arr)):
        yield arr[x]

def main():
    gen = generator_with_list()
    for x in range(10):
        print( next(gen) )
        time.sleep(0.5)

if (__name__ == "__main__"):
    main()