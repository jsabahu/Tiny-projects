import time

def methodNativeDict(unsorted: list) -> (list, float):
    '''
    '''
    t0 = time.time()
    
    checked = []
    d = {}
    for number in unsorted:
        if number in checked:
            continue
        else:
            d[number] = unsorted.count(number)
            checked.append(number)
    t1 = time.time() - t0

    return [[k, v] for k,v in d.items()],t1

if __name__ == "__main__":
    numbers = [1,2,3,1,2,4]
    print(methodNativeDict(numbers))