
def threshold(h, Y):
    return {t : Y[t] for t in Y if Y[t] >= h}

def times(Y):
    return Y.keys()
