import numpy as np

def info_nce_loss(Z1: list, Z2: list, temperature: float = 0.1) -> float:
    """
    Returns the loss as a float.
    """
    z1 = np.asarray(Z1, dtype=np.float64)
    z2 = np.asarray(Z2, dtype=np.float64)
    S=(z1 @ z2.T)/temperature

    logd=np.logaddexp.reduce(S,axis=1)
    pos=np.diag(S)

    return float(np.mean(logd-pos))
    