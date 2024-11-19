
def factorial(n):
    """
    Calculates the factorial of a given non-negative integer.

    The factorial of a non-negative integer `n` is defined as:
    n! = n * (n-1) * (n-2) * ... * 1, with the special case 0! = 1.

    If the input number is negative, the function returns 0 as factorial 
    is not defined for negative numbers.

    Args:
        n (int): The non-negative integer for which the factorial is calculated.

    Returns:
        int: The factorial of the given number `n`, or 0 if `n` is negative.

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(-3)
        0
    """
    if n < 0:
        return 0
    elif n==1 or n == 0:
        return 1
    else:
        toReturn = 1
        while (n>1):
            toReturn *= n
            n -= 1
        return toReturn
print(factorial(5))


[THIS IS MY GITHUB REPO LINK](https://github.com/SafanurRafi/ecPycharm).
