#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/23 9:48
# @Author  : 杨再润
# @Site  :  https://tim-saijun.github.io/
import numpy as np
from core.model import Model

def normalise_windows(window_data, single_window=False):
    normalised_data = []
    window_data = [window_data] if single_window else window_data
    for window in window_data:
        normalised_window = []
        for col_i in range(window.shape[1]):
            normalised_col = [((float(p) / float(window[0, col_i])) - 1) for p in window[:, col_i]]
            normalised_window.append(normalised_col)
        normalised_window = np.array(
            normalised_window).T
        normalised_data.append(normalised_window)
    return np.array(normalised_data)

def inference(x):
    x= np.array(x)
    y = normalise_windows(x,True)
    y = np.array(y)
    # print(y.shape) #(1, 9, 3)
    # print(x[0][0],x[0][1],x[0][2]) #5.0 2.0 3.0

    model = Model()
    model.load_model("saved_models/22122022-175706-e2.h5")
    pred = model.predict_point_by_point(y)
    pred = (pred+1)*x[0][0] #逆正则化
    # print(pred)
    return pred

if __name__ == '__main__':
    x = [
        [5, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 7],
        [7, 8, 9],
        [0.7, 1, 2],
        [10, 2, 3],
        [6, 6, 6]
    ]
    print(inference(x))
