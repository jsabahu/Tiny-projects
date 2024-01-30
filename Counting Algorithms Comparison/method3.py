import time

def method3(unsorted: list) -> (list, float):
    '''
    This function takes an unsorted list of numbers as input and returns a tuple of two elements as output. 
    The first element is a list of sublists, each containing a unique number from the input list and its frequency. 
    The second element is the elapsed time of the function in seconds. 
    
    The function uses two nested for loops to iterate through the input list and the noduplis list, 
    which stores the unique numbers from the input list. 
    
    It also uses the time module to measure the performance of the function.
    '''
    t0 = time.time()
    noduplis = []
    numveces = []
    for i in unsorted:
        if i not in noduplis:
            noduplis.append(i)
    for x in noduplis:
        counter = 0
        for num in unsorted:
            if num == x:
                counter = counter + 1
        numveces.append([x, counter])
    t1 = time.time() - t0
    return numveces, t1

if __name__ == "__main__":
    numbers = [1,2,3,1,2,4]
    print(method3(numbers))