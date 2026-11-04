import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    xa=np.asarray(x)
    return np.where(xa>=0,1/(1+np.exp(-xa)),np.exp(x)/(1+np.exp(xa)))
    pass