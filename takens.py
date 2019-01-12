#!/usr/bin/python3

# ****************************************************
# Create takens embedding
#
# S:    time-series in dictionary form
# d:    dimension of embedding
# tau:  delay, how far back in the time-series to look
# ****************************************************
def Takens(S, d, tau):
   
    if d < 1:
        print("d must be greater than or equal to 1")
        return

    if tau < 1:
        print("tau must be greater than or equal to 1")
        return

    T = []
    for i, (t, value) in enumerate(S.items()):
        if (i+1)%tau == 0:
            temp = []
            for j in range(0, d):
                try:
                    temp = [S.get(t-((j*tau)/d))] + temp
                except TypeError:
                    print("d and tau must be integers greater than one")
            T.append(temp)
            
    return T
