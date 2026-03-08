def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    total = sum(numbers)
    # The bug is here: no check for empty list (DivisionByZero)
    return total / len(numbers)
