def acc(yhat, y):
    import numpy as np
    acc = np.mean(yhat == y)
    return acc

def rmse(yhat, y):
    import numpy as np
    RMSE = np.sqrt(np.mean(  (yhat - y)**2  ))
    return RMSE

def r2(yhat, y):
    SSres = ((yhat - y)**2).sum()
    SStot = ((y - y.mean())**2).sum()
    R2 = 1 - SSres/SStot
    return R2