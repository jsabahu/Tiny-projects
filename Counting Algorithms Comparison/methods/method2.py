import time

def method2(unsorted: list) -> (list, float):
    '''
    This function takes an unsorted list of numbers as input and returns a tuple of two elements as output. 
    The first element is a list of sublists, each containing a unique number from the input list and its frequency. 
    The second element is the elapsed time of the function in seconds. 

    The function uses a for loop and the enumerate function to iterate through the input list and count the occurrences of each number. 
    It also uses a checked list to avoid counting the same number twice. 
    
    It also uses the time module to measure the performance of the function.
    '''
    t0 = time.time()
    replist = []
    checked = []
    for pos, numcheck in enumerate(unsorted):
        counter = 1
        if numcheck in checked:
            continue
        else:
            for y in unsorted[pos+1:]:
                if y == numcheck:
                    counter = counter + 1
        replist.append([numcheck, counter])
        checked.append(numcheck)
    t1 = time.time() - t0
    return replist, t1

if __name__ == "__main__":
    numbers = [1,2,3,1,2,4]
    print(method2(numbers))