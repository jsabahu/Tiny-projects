from methods.method1 import method1
from methods.method2 import method2
from methods.method3 import method3
from methods.method4 import method4

from methods.methodBuiltIn import methodBuiltIn
from methods.methodBuiltInDict import methodBuiltInDict

import random
from statistics import mean
import numpy as np

from utils import progressbar
from buildGif import rotanimate

import matplotlib.pyplot as plt # import the matplotlib module for plotting

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

    random.seed(42) ### reset random numbers

    for length in progressbar(range(10, listLength, step), "Computing: ", 40):

        for rang in range(10, listDomain,step):

            m = []
            for i in range(timesMean):
                numbers = []
                for j in range(length):
                    numbers.append(random.randint(0,rang))

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
    X4, Y4, Z4 = testMethod(listLength, listDomain, timesMean, step, method4) # results for method4
    Xn, Yn, Zn = testMethod(listLength, listDomain, timesMean, step, methodBuiltIn) # results for methodNative
    Xnd, Ynd, Znd = testMethod(listLength, listDomain, timesMean, step, methodBuiltInDict) # results for methodNativeDict

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
    ax.plot_trisurf(X4, Y4, Z4, color='white', edgecolors='grey', alpha=0.5)
    ax.scatter(X4, Y4, Z4, c='purple', label='method 4')
    ax.plot_trisurf(Xn, Yn, Zn, color='white', edgecolors='grey', alpha=0.5)
    ax.scatter(Xn, Yn, Zn, c='black', label='method Native')
    ax.plot_trisurf(Xnd, Ynd, Znd, color='white', edgecolors='grey', alpha=0.5)
    ax.scatter(Xnd, Ynd, Znd, c='yellow', label='method Native Dict')

    angles = np.linspace(0,360,101)[:-1] # Take 100 angles between 0 and 360

    # create an animated gif (10ms between frames)
    rotanimate(ax, angles,'movie.gif',delay=10)
    

if __name__ == "__main__":
    main()