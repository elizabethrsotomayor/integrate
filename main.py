def integrate(coefficient: int, exponent: int) -> str:
    """
    Create a function that finds the integral of the expression passed.
    :param coefficient:
    :param exponent:
    :return:
    """
    integral = coefficient / (exponent + 1)
    return "x^".join((str(int(integral)), str(exponent + 1)))
