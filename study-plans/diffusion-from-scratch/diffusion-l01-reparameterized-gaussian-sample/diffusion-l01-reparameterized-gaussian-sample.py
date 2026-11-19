import numpy as np

def reparameterized_sample(mean: np.ndarray, log_variance: np.ndarray, noise: np.ndarray) -> np.ndarray:
    """
    Returns the reparameterized samples as a float64 array with the broadcast shape of the inputs.
    """
    std = np.sqrt(np.exp(log_variance))
    z = np.add(mean,np.multiply(std,noise))
    return z.astype(np.float64)