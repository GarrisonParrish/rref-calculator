# rref-calculator
Converts an augmented matrix to row-reduced echelon form

Many thanks to my Linear Algebra professor for explaining the row reduction algorithm and making many
not-so-subtle hints to the fact that a computer could do all this. I know Matlab does this in like 2 seconds but I
want to use my brain, dang it!

## Project goals:
- prompt user for input on command line
- Define number of rows and columns, then prompt for value in each cell
- Use the algorithm to convert the matrix to row-reduced echelon form
- print output in a clean, easy-to-read format

## Algorithm:
1. Start at top right cell
2. Eliminate all cells below (make them 0 using the following elementary row operations:
- Multiply rows by a nonzero scalar
- Add rows
- Swap rows
3. Move down and to the right
4. repeat until the last pivot is 1

**NOTE: There are many variations in the form that must be accounted for. The algorithm must decide on the best next choice
at each step. There may be multiple steps to clear a column and move to the next row. We want to reach the solution in
as few moves as possible.**

Fractions may present an issue, as will floating-point error in arithmetic operations.
