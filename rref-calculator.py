"""This program will convert a matrix to row-reduced echelon form."""

def main():
    matrix = matrix_input()


def matrix_input():
    """Prompts the user for dimensions of the matrix and value in each cell."""
    # Use nested lists to represent a matrix. Example: matrix: int[int[]] = [[1, 2], [3, 4]]

    row_len: int = int(input('Number of rows: '))
    col_len: int = int(input('Number of columns: '))
    matrix: int[int[col_len]] = []

    
    for r in range(0, row_len):
        # Make a new empty list
        matrix.append([])
        print(f'ROW { r }:')
        for c in range(0, col_len):
            # print(f'{ r }, { c }')
            # Add elements to the empty list for this row
            element: int = int(input(f'Element at ({ r }, { c }): '))
            matrix[r].append(element)
    # At this point we have a matrix with all elements 0. This is an intermediate step and there is likely a more
    # efficient way to do this once we have our elements.

    # Now, prompt the user for input in each cell
    
    print(matrix)
    # Thank God for Python's weird ability to not define return types in function declarations
    return matrix

def rref_calculator(matrix):
    """Applies algorithm to convert matrix to row-reduced echelon form."""

    # Time to consult that interesting algorithm I got from Purdue's website

if __name__ == "__main__":
    main()