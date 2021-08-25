from fractions import Fraction
import fractions

"""It's come to my attention that this program will be vastly more complex than I initially assumed."""

# Need to figure out how to make it do algebra first.
# There are libraries for this
# Not the whole entirety of algebra, just a simple algebraic equation solver for expressions with one variable.


# Ex: 2x + 5 = 10
# 2x = 5
# x = 5/2 FINISHED: output as 5/2
# THis will definitely need an algebra library

Y = 10
M = 2
B = 5


def main():
    # ans: float = equation_solver(Y, M, B)
    print(float_to_frac(5.5))


def equation_solver(y: float, m: float, b: float) -> float:
    """Input a y value, a coefficient, and a y-intercept in y = mx + b form, output a float."""
    # y = m*x + b
    # x = ?
    return (y - b) / m

def float_to_frac(input: float) -> str:
    """Input a float and output a fraction as a formatted string."""
    # https://www.mathsisfun.com/converting-decimals-fractions.html

    # 1. Write as float/1
    # 2. Multiply by 10 until the float is a whole number (float.is_integer())
    # 3. Try to reduce until we can't reduce anymore

    denom: float = 1
    while (input.is_integer() == False):
        input *= 10
        denom *= 10

    # Now we have our input and denom
    # print(f'{input} / {denom}')

    # Screw it we're using a library
    # https://stackoverflow.com/questions/17537613/does-python-have-a-function-to-reduce-fractions
    return str(Fraction(int(input), int(denom)))


if __name__ == '__main__':
    main()