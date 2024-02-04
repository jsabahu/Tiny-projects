
# Counting Algorithms Comparison

In this small python project we will see the performance (time) of different counting algorithms within different lists of numbers. Below we will see the different methods used:

## Methods

- ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) `Method 1`
This method uses a while loop as long as the list contains at least one number. Inside the loop we select the first number in the list and iterate through all the remaining numbers with a for loop. If any of the remaining ones are the same as the first, we increase the counter by 1 and remove them from the list.
We repeat this process until the list is empty.

- ![#008000](https://placehold.co/15x15/008000/008000.png) `Method 2`
This second method uses a for loop to iterate through the list of numbers and counts the number of occurrences for each number. We use a "checked" list to avoid counting the same number more than once.

- ![#0000FF](https://placehold.co/15x15/0000FF/0000FF.png) `Method 3`
  This third method uses two nested for loops to iterate through the input list and the <em>'noduplis'</em> list, which stores the unique numbers from the input list.

- ![#A020F0](https://placehold.co/15x15/A020F0/A020F0.png) `Method 4`
  This fourth method uses a dictionary to count the frequency of unique items in the list. This gives it great performance, since it updates the counters within the dictionary as it goes through the list. So it only goes through the list 1 time.
  
- ![#1589F0](https://placehold.co/15x15/000000/000000.png) ![#FFFF00](https://placehold.co/15x15/FFFF00/FFFF00.png) `Built-In Method`
  The last method uses the built-in count function to count the occurrences of each number non checked before. 


## Acknowledgements

 - [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)


## Authors

- [@jsabahu](https://www.github.com/jsabahu)


## Screenshots

![App Screenshot](https://github.com/jsabahu/Tiny-projects/blob/main/CountingAlgorithmsComparison/figures/300_300_100_10.gif)

