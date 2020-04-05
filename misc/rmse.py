"""
predicted = [4,25,0.75,11]
observed = [3,21,-1.25,13]
return rmse of the two lists using numpy functions
"""

def Solution(predicted, observed):
    pred_arr = np.array(predicted)
    obs_arr = np.array(observed)
    return np.sqrt(((pred - obs) ** 2).mean())

predicted = [4, 25, 0.75, 11]
observed = [3, 21, -1.25, 13]
Solution(predicted, observed) 