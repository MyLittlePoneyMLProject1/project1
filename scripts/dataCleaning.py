import numpy as np

#Removing the rows where there is a -999 value for the selected features

#Return the index and the variables without 999 values
def remove_rows_variable(tX):
    boo = [not((tX[i] == -999).any()) for i in range(tX.shape[0])]
    ind = np.where(boo)[0]
    return ind,tX[ind]

def remove_rows_all(tX,y):
    boo = [not((tX[i] == -999).any()) for i in range(tX.shape[0])]
    ind = np.where(boo)[0]
    return ind,tX[ind],y[ind]

def remove_features_999(tX):
    
    tX_wto_999_features = tX
    for i in reversed(range(tX.shape[1])):
        if(-999 in tX[:,i]):
            tX_wto_999_features = np.delete(tX_wto_999_features, i, 1)  # delete i-th column
    
    return tX_wto_999_features