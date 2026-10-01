




import numpy as np


def f(x,     y    ):
    d = {"a": 1, "b": 2}
    if x > y:
             return np.sqrt(x**2 + y**2), d
    else:
        return x + y, d


result = f(3, 4)
print(result)
