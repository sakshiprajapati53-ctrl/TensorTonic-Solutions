import numpy as np
import math
def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    row,col = X.shape
    weights = np.zeros(col)
    bias = 0.0
    for _ in range(steps):
        p = _sigmoid(np.matmul(X, weights) + bias)
        deriv_weight = (1/row) * np.matmul(np.transpose(X), (p - y))
        deriv_bias = (1/row) * np.sum(p - y)
        weights = weights - lr * deriv_weight
        bias = bias - lr * deriv_bias
    return weights, bias    
    