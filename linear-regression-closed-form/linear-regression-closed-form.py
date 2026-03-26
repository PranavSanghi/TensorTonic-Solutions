import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    X=np.array(X)
    y=np.array(y)
    temp = X.T @ X
    temp1 = np.linalg.inv(temp)
    w = temp1 @ X.T @ y
    return w 
    # Write code here
    pass