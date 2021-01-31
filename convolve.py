
import torch
import torch.nn as nn
import numpy as np


class Net(nn.Module):
    def __init__(self, np_weights):
        super(Net, self).__init__()
        stride = 1
        in_channels = out_channels = 1
        kernel_size = np_weights.shape[2]
        padding = int(kernel_size/2)
        in_channels = np_weights.shape[1]
        self.conv = nn.Conv1d(in_channels, out_channels, kernel_size, stride, padding, bias=False)
        FloatTensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor
        self.conv.weight = nn.Parameter(FloatTensor(np_weights))

    def forward(self, x):
        x = self.conv(x)
        return x



def conv_signal(np_weight, signal):
    with torch.no_grad():
        np_weight = np.expand_dims(np_weight, axis=0)  # batch
        np_weight = np.expand_dims(np_weight, axis=0)  # channels

        signal = np.expand_dims(signal, axis=0)  # batch
        signal = np.expand_dims(signal, axis=0)  # channels

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = Net(np_weight).to(device)
        model.eval()

        FloatTensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor
        data = (FloatTensor(signal)).to(device)
        output = model(data).cpu().detach().numpy()
        output = np.squeeze(output, 0)
        output = np.squeeze(output, 0)
        return output
    return None



if __name__ == "__main__":
    np_weight = np.array([0.,1.,0.])
    signal = np.array([1,2,3,4,5,6,7,8])
    result = conv_signal(np_weight, signal)
    print(result )
    # prints [1. 2. 3. 4. 5. 6. 7. 8.]