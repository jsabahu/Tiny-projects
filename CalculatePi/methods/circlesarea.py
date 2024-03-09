from random import randrange
from math import sqrt

def computePi(radius, iter, save_logs=None) -> int:
    '''Source: https://en.wikipedia.org/wiki/Approximations_of_%CF%80'''

    r = radius
    total_points = 0
    inside_points = 0
    pi_records = []

    for i in range(iter):
        point_x = randrange(0,r,1)
        point_y = randrange(0,r,1)

        total_points += 1
    
        if (sqrt((point_x**2) + (point_y**2)) <= r):
            inside_points += 1
        if save_logs:
            if i % save_logs == 0:
                pi_records.append(inside_points*4 / total_points)

    pi = inside_points*4 / total_points   
    if save_logs:
        return pi, pi_records
    else:
        return pi, []
    


if __name__ == '__main__':
    pi, pi_records = computePi(10000000, 10**7)
    print(pi)
