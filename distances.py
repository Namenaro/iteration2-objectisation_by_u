import math
import numpy as np

def apply_device_to_signal(np_weight, signal):
    res = []
    win_len = len(np_weight)
    half_win = int(win_len/2)
    sig_len = len(signal)
    signal = np.pad(signal, (half_win, half_win), 'constant')
    for i in range(half_win, sig_len+half_win):
        patch = signal[i-half_win:i+half_win]
        dist = math.dist(np_weight, patch)
        res.append(dist)
    return np.array(res)

if __name__ == "__main__":
    np_weight = np.array([1,1])
    signal = np.array([0,1,2,5,8])
    res = apply_device_to_signal(np_weight, signal)
    print(res)
    # prints [1.41421356 1.         1.         4.12310563 8.06225775]






