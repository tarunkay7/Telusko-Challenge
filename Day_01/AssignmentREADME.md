<h1>Problem Statement : Implement the Pascals Triangle iteratively,recursively and and using memoization</h1>

<h2> Iterative Implementation</h2>
The function will take the number of rows as input and then it will initialize an empty list called tri first to store the triangle. It then iterates from 0 to num_rows - 1 and builds each row.


For each row what it does means it starts with a list containing a single element, which is 1. If the triangle already has some rows, it will get back the previous row and calculates the elements of the current row based on the previous row. It iterates over the elements of the previous row and adds the two adjacent elements to create the current element. It then appends 1 at the end of the row.


In last step it adds the current row to the list. After the iteration completes, it returns the triangle list containing Pascal's triangle.

<h2> Recursive Implementation</h2>

The base case is when num_rows is 1. In this case, we return a single-row triangle [[1]].

For num_rows greater than 1, we make a recursive call to pascals_triangle_recursive(num_rows - 1) to generate the triangle with num_rows - 1 rows. We store this triangle in the variable triangle.

After that we retrieve last row of triangle and store it in prev_row. We create a new row list starting with 1.

We then iterate over the elements of prev_row (except the last one) and calculate the elements of the current row by adding each pair of adjacent elements. We append 1 to the end of the row to complete it.
Then we append the newly generated row to the triangle list and return it.

<h2> Memoization Implementation</h2>
The base case remains the same as before when num_rows is 1, where we return a single-row triangle [[1]].

Before making the recursive call, we check if the result for the current num_rows is already present in the memo dictionary.

If the result is not present in the memo dictionary, we proceed with the recursive call to pascals_triangle_memo for num_rows - 1 and store the result in the triangle variable.

After generating the triangle, we store it in the memo dictionary with the current num_rows as the key
then we return the triangle.

This way we can retrieve the triangle from the memo dictionary instead of recomputing it, which helps improve efficiency.


<h2>Time complexities</h2>
The time complexitites of making a pascals triangle are all O(num_rows^2) but using memoization we can make the algorithm very efficent in terms of computing power.


