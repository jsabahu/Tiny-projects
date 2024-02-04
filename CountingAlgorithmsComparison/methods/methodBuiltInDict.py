import time

def methodBuiltInDict(unsorted: list) -> (list, float):
    '''
    Given an unsorted list of numbers, this function computes the frequency count of each unique element and returns a list of lists containing the unique elements along with their corresponding counts. 
    It uses a dictionary and the built-in function 'count'.
    Additionally, it measures the time taken for this computation.
    Counts the frequency of elements in an unsorted list using a dictionary and the built-in function 'count'.

    Args:
        unsorted (list): An unsorted list of elements.

    Returns:
        tuple: A list of lists containing unique elements and their corresponding frequencies,
               and the time taken for the operation in seconds.

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