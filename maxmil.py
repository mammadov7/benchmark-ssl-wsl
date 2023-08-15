import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class maxmil(nn.Module):
    def __init__(self, input_size):
        super(maxmil, self).__init__()
        self.L = input_size
        self.D = input_size
        self.K = 1

        self.classifier =  nn.Linear(self.L*self.K, 1)
       

    def forward(self, x): # N,D
        Y_probs = self.classifier(x)
        Y_prob = torch.amax(Y_probs, dim=0, keepdim=True)  # KxL
        Y_hat = torch.ge(Y_prob, 0.5).float()
        num_inst, dim = x.shape
        A = torch.ones((1, num_inst)).to(x.device)
        return Y_prob, A