import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    array = np.array(list).reshape(3, 3)

    #MEAN 
    mean_axis0 = np.mean(array , axis=0).tolist()
    mean_axis1 = np.mean(array, axis=1).tolist()
    mean_flattened = np.mean(array).item()

    #VARIANCE
    var_axis0 = np.var(array , axis=0).tolist()
    var_axis1 = np.var(array , axis=1).tolist()
    var_flattened = np.var(array).item()

    #STANDARD DEVIATION
    std_dv_axis0 = np.std(array, axis=0).tolist()
    std_dv_axis1 = np.std(array , axis=1).tolist()
    std_dv_flattened = np.std(array).item()

    #MAX
    max_axis0 = np.max(array , axis=0).tolist()
    max_axis1 = np.max(array , axis=1).tolist()
    max_flattened = np.max(array).item()

    #MIN
    min_axis0 = np.min(array , axis=0).tolist()
    min_axis1 = np.min(array , axis=1).tolist()
    min_flattened = np.min(array).item()

    #SUM
    sum_axis0 = np.sum(array, axis=0).tolist()
    sum_axis1 = np.sum(array , axis=1).tolist()
    sum_flattened = np.sum(array).item()

    calculations = {
        'mean': [mean_axis0, mean_axis1,mean_flattened],
        'variance': [var_axis0, var_axis1, var_flattened],
        'standard deviation':[std_dv_axis0, std_dv_axis1, std_dv_flattened],
        'max': [max_axis0, max_axis1, max_flattened],
        'min': [min_axis0, min_axis1, min_flattened],
        'sum': [sum_axis0, sum_axis1, sum_flattened]
    }

    return calculations
