import time

def method4(unsorted: list) -> (list, float):
    '''
      Given an unsorted list of numbers, this function computes the frequency count of each unique element and returns a list of lists containing the unique elements along with their corresponding counts. 
      It uses a dictionary to count the frequency. This method only goes through the list once.
      Additionally, it measures the time taken for this computation.

    Args:
        unsorted (list): An unsorted list of numbers.

    Returns:
        tuple: A tuple containing two elements:
            - A list of lists, where each inner list contains two elements: the unique element and its count in the input list.
            - A float representing the time taken for the computation in seconds.
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