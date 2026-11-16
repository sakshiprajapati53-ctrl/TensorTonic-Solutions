import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    dot_prod = np.dot(a,b)
    mod = np.linalg.norm(a)*np.linalg.norm(b)
    if (int(mod) == 0):
        return float(0)
    return float(dot_prod/mod)
    