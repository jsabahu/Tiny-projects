import time

def method4(unsorted: list) -> (list, float):
    '''
    '''
    t0 = time.time()
    d = {}
    for n in unsorted:
        d[n] = d.get(n, 0) + 1
    t1 = time.time() - t0

    return [[k, v] for k,v in d.items()],t1

if __name__ == "__main__":
    numbers = [1,2,3,1,2,4]
    print(method4(numbers))