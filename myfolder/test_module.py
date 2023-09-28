
import numpy as np
def test_function(x):
    B = [x **10 for x in range(10000)]
    C = np.array(B)
    C * 20000
    return C[0] 
