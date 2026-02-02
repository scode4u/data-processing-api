import numpy as np

def to_python(value):
    if isinstance(value, np.generic):
        return value.item()
    return value
