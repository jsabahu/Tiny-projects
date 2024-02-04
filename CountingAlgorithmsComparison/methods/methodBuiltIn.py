import time

def methodBuiltIn(unsorted: list) -> (list, float):
    '''
    This function takes an unsorted list of numbers as input and returns a tuple of two elements as output. 
    The first element is a list of sublists, each containing a unique number from the input list and its frequency. 
    The second element is the elapsed time of the function in seconds. 

    The function uses the native count function to count the occurrences of each number. 
    
    It also uses the time module to measure the performance of the function.
    '''
    t0 = time.time()
    replist = []
    checked = []
    for number in unsorted:
        if number in checked:
            continue
        else:
            replist.append([number, unsorted.count(number)])
            checked.append(number)
    t1 = time.time() - t0
    return replist, t1

if __name__ == "__main__":
    numbers = [1,2,3,1,2,4]
    print(methodNative(numbers))