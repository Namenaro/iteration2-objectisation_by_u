from utils import get_7_helthy_json, get_points, get_lead_signal
from distances import apply_device_to_signal
from visualise_ecg import VisualECG


import matplotlib.pyplot as plt

def get_raw_kernel():
    json_data = get_7_helthy_json()
    json_node = json_data[list(json_data.keys())[0]]
    points = get_points(json_node, "qrs", 1)
    point = points[1]
    signal = get_lead_signal(json_node, 'i')
    from_= point - 100
    to_ = point + 100
    return signal[from_:to_]

if __name__ == "__main__":
    np_weight = get_raw_kernel()
    json_data = get_7_helthy_json()

    for key in json_data.keys():
        json_node = json_data[key]
        vis = VisualECG(json_node)
        signal = get_lead_signal(json_node, 'i')
        res = apply_device_to_signal(np_weight, signal)
        vis.ecg_with_additional_signal(res, 0, 4999,['i','ii'])
        plt.show()
