def rmse(yhat, y):
    import numpy as np
    RMSE = np.sqrt(np.mean(  (yhat - y)**2  ))
    return RMSE

def acc(yhat, y):
    import numpy as np
    acc = np.mean(yhat == y)
    return acc

def r2(yhat, y):
    SSres = ((yhat - y)**2).sum()
    SStot = ((y - y.mean())**2).sum()
    r2 = 1 - SSres/SStot
    return r2

def stdz(vector):
    import numpy as np
    std_vec = (vector - np.mean(vector))/np.std(vector)
    return std_vec