import numpy as np
import math

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    dot_product = float(math.sumprod(x,y))
    return dot_product