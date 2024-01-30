from method1 import method1
from method2 import method2
from method3 import method3

import time
import sys

from random import randint
from statistics import mean

import matplotlib.pyplot as plt # import the matplotlib module for plotting

def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.6+
    '''https://stackoverflow.com/questions/3160699/python-progress-bar'''
    count = len(it)
    start = time.time()
    def show(j):
        x = int(size*j/count)
        remaining = ((time.time() - start) / j) * (count - j)
        
        mins, sec = divmod(remaining, 60)
        time_str = f"{int(mins):02}:{sec:05.2f}"
        
        print(f"{prefix}[{u'█'*x}{('.'*(size-x))}] {j}/{count} Est wait {time_str}", end='\r', file=out, flush=True)
        
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

def testMethod(listLength: int, listDomain: int, timesMean: int, step: int, method):

    '''
    This function takes four parameters: listLength, listDomain, timesMean, and step, as well as a method to test. 
    The function uses nested for loops to generate random numbers and apply the method to them. 
    It also calculates the mean of the elapsed time of the method for each combination of length and domain.
    
    The X list contains the values of length, which are the lengths of the random lists. 
    The Y list contains the values of domain, which are the domains of the random numbers. 
    The Z list contains the values of mean(m), which are the average elapsed times of the method for each pair of length and domain.

    The function is useful for testing the performance of the different methods for sorting and counting the frequency of numbers in a list.
    '''

    X = [] #lengthList
    Y = [] #domainList
    Z = [] #samplingResultsList

    for length in progressbar(range(10, listLength, step), "Computing: ", 40):

        for rang in range(10, listDomain,step):

            m = []
            for i in range(timesMean):
                numbers = []
                for j in range(length):
                    numbers.append(randint(0,rang))

                _, t = method(numbers.copy())
                m.append(t)

            X.append(length)
            Y.append(rang)
            Z.append(mean(m))

    return X, Y, Z



def main():
    # define the parameters for the testMethod function
    listLength = 300 # the maximum length of the random lists
    listDomain = 300 # the maximum domain of the random numbers
    timesMean = 100 # the number of times to repeat the method for each pair of length and domain
    step = 10 # the step size for increasing the length and rang

    # apply the testMethod function to each method and store the results in variables
    X1, Y1, Z1 = testMethod(listLength, listDomain, timesMean, step, method1) # results for method1
    X2, Y2, Z2 = testMethod(listLength, listDomain, timesMean, step, method2) # results for method2
    X3, Y3, Z3 = testMethod(listLength, listDomain, timesMean, step, method3) # results for method3

    # plot the results using a scatter-plane 3D plot with different colors for each method

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('Length')
    ax.set_ylabel('Domain')
    ax.set_zlabel('Avg t [s]')

    ax.plot_trisurf(X1, Y1, Z1, color='white', edgecolors='grey', alpha=0.5)
    ax.scatter(X1, Y1, Z1, c='red', label='method 1')
    ax.plot_trisurf(X2, Y2, Z2, color='white', edgecolors='grey', alpha=0.5)
    ax.scatter(X2, Y2, Z2, c='green', label='method 2')
    ax.plot_trisurf(X3, Y3, Z3, color='white', edgecolors='grey', alpha=0.5)
    ax.scatter(X3, Y3, Z3, c='blue', label='method 3')
    ax.legend() # show the legend
    plt.show() # show the plot
    

if __name__ == "__main__":
    main()