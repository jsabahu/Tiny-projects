import time

def method1(unsorted: list) -> (list, float):
    '''
    This function takes an unsorted list of numbers as input and returns a tuple of two elements as output. 
    The first element is a list of sublists, each containing a unique number from the input list and its frequency. 
    The second element is the elapsed time of the function in seconds. 
    
    The function uses a while loop and a for loop to iterate through the input list and count the occurrences of each number. 
    
    It also uses the time module to measure the performance of the function.
    '''
    t0 = time.time()
    replist = []
    while len(unsorted)!=0:
        counter = 0
        numcheck=unsorted.pop(0)
        counter = counter + 1
        for i in unsorted.copy():
            if i == numcheck:
                counter = counter + 1
                unsorted.remove(i)
            else:
                continue
        replist.append([numcheck, counter])
    t1 = time.time() - t0

    return replist, t1

if __name__ == "__main__":
    numbers = [1,2,3,1,2,4]
    print(method1(numbers))