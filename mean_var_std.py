import numpy as np

def calculate(list):


    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    array_3x3 = np.asarray(list).reshape((3,3))
    axis1 = np.mean(array_3x3, axis=0).tolist()
    axis2 = np.mean(array_3x3, axis=1).tolist()
    flattened = np.mean(array_3x3).tolist()
    axis1_2 = np.var(array_3x3, axis=0).tolist()
    axis2_2 = np.var(array_3x3, axis=1).tolist()
    flattened_2 = np.var(array_3x3).tolist()
    axis1_3 = np.std(array_3x3, axis=0).tolist()
    axis2_3 = np.std(array_3x3, axis=1).tolist()
    flattened_3 = np.std(array_3x3).tolist()
    axis1_4 = np.max(array_3x3, axis=0).tolist()
    axis2_4 = np.max(array_3x3, axis=1).tolist()
    flattened_4 = np.max(array_3x3).tolist()
    axis1_5 = np.min(array_3x3, axis=0).tolist()
    axis2_5 = np.min(array_3x3, axis=1).tolist()
    flattened_5 = np.min(array_3x3).tolist()
    axis1_6 = np.sum(array_3x3, axis=0).tolist()
    axis2_6 = np.sum(array_3x3, axis=1).tolist()
    flattened_6 = np.sum(array_3x3).tolist()

    calculations = {
        'mean': [axis1, axis2, flattened],
        'variance':[axis1_2, axis2_2, flattened_2],
        'standard deviation': [axis1_3, axis2_3, flattened_3],
        'max': [axis1_4, axis2_4, flattened_4],
        'min': [axis1_5, axis2_5, flattened_5],
        'sum': [axis1_6, axis2_6, flattened_6]
    }


    return calculations



