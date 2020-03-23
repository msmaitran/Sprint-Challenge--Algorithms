#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) **O(n)**
The number of times the loop runs varies based on the value of *n*.
As the size of the input increases, the runtime or space used will grow at the same rate.

b) **O(log n)**
Outer loop runs *n* times, inner loop factor increases by 2.
As the size of the input increases, the runtime or space used will grow at a slightly slower rate.

c) **O(n)**
Recursive function that calls itself. Runs through all the data once.

## Exercise II

**Binary Search: O(log n)**
1. Find the current_middle:
    * current_middle = (max - min) // 2
        * *max = highest floor*
        * *min = lowest floor*
2. Drop the egg from the current_middle floor:
    * If the egg breaks:
        * Find the new_middle:
            * new_middle = (current_middle - min) // 2
    * If the egg does not break:
        * Find the new_middle:
            * new_middle = (max - current_middle) // 2
3. Repeat step 2 until the egg does not break at the highest floor, *f*.