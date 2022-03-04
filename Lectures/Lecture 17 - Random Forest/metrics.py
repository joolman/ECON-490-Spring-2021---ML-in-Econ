def acc(yhat, y):
    import numpy as np
    acc = np.mean(yhat == y)
    return acc

def rmse(yhat, y):
    import numpy as np
    RMSE = np.sqrt(np.mean(  (yhat - y)**2  ))
    return RMSE