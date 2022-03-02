import numpy as np
import torch
from dgl import DGLGraph

def Approx_prefix(input_features, parameter=0.5):
    '''
    Approx_results -> the first parameter*length values of the feature
    '''
    scale = int(input_features.size(1)*parameter)
    approx_results = input_features[:, :scale]
    return approx_results