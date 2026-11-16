import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    return float(sum(abs(float(x_i) - float(y_i)) for x_i, y_i in zip(x, y)))