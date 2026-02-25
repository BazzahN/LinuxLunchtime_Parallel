import numpy as np

def matexp(X,m) :
    '''
    Approximates the matrix exponenital of X using m terms.

    Inputs
    ------
        X: numpy.Array
            The matrix to be operated on
        m: int
            The number of terms in the approximate sum

    Returns
    -------
        Y: numpy.array
            The squared exponential of X 
    '''
    n,_ = np.shape(X)
    Z = np.identity(n)
    Y = Z
    for k in range(1,m) :
        Z = np.matmul(Z,X)/k
        Y = np.add(Y,Z)
    return Y
