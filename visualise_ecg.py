from utils import get_lead_signal, get_ecg_description, get_points

import matplotlib.pyplot as plt

class VisualECG:
    def __init__(self, ecg_node):
        self.ecg_node = ecg_node

    def ecg_to_fig(self, leads_names, from_, to_):
        numleads = len(leads_names)
        fig, axs = plt.subplots(numleads, 1, figsize=(8, 2 * numleads), sharex=True, sharey=True)
        axs = axs.ravel()

        for i in range(numleads):
            name = leads_names[i]
            signal = get_lead_signal(self.ecg_node, name)[from_:to_]
            axs[i].plot(signal)
            axs[i].set_title(name)
        plt.title(get_ecg_description(self.ecg_node))
        return fig

    def show_component(self, from_, to_, leads_names, component):
        centers = get_points(self.ecg_node, component, n_in_triple=1)
        center = centers[1]
        from_ = center - from_
        to_ = center + to_
        self.ecg_to_fig(leads_names, from_, to_)
        plt.show()

    def ecg_with_additional_signal(self, other_channel, from_, to_, leads_names):
        numleads = len(leads_names)
        fig, axs = plt.subplots(numleads+1, 1, figsize=(8, 2 * (numleads+1)), sharex=False, sharey=False)
        axs = axs.ravel()

        axs[0].plot(other_channel[from_:to_],'r')
        for i in range(1, numleads+1):
            name = leads_names[i-1]
            signal = get_lead_signal(self.ecg_node, name)[from_:to_]
            axs[i].plot(signal)
            axs[i].set_title(name)
        #plt.title(get_ecg_description(self.ecg_node))
        return fig

if __name__ == "__main__":
    from utils import get_7_helthy_json
    json_data = get_7_helthy_json()

    for key in json_data.keys():
        json_node = json_data[key]
        vis = VisualECG(json_node)
        #vis.ecg_to_fig(["i","ii"],0, 300)
        vis.show_component(from_=50, to_=50, leads_names=['i','ii'], component='qrs')
        plt.show()
