#-*- coding: utf-8 -*-

r"""
    @Copyright 2022 
    The Intelligence Data Analysis, in DKU. All Rights Reserved.    
"""

import torch
import torch.nn as nn
import torchsummary
import collections

r"""
    [Examples]
    for load model and print model structure
        model = LeNet(in_channels=1, num_classes=1000).cuda()
        torchsummary.summary(model, input_size=(1,28,28))
"""

class ShallowNet(nn.Module):
    r"""
        Return the torch modules, containing shallowNet model.
        
        Args:
            in_channels : the number of channels included in input data.
            num_classes : the number of classes.
    """
    def __init__(self, in_channels=3, num_classes=1000):
        super(ShallowNet, self).__init__()

        self.ConvBlock_0 = nn.Sequential(
                collections.OrderedDict([
                    ("Conv2d_0", nn.Conv2d(
                        in_channels = in_channels,
                        out_channels = 32,
                        kernel_size = 3,
                        stride = 1,
                        padding =1)),
                    ("Activation_0", nn.ReLU()),
                    ("Flatten", nn.Flatten()),
                    ("FC_0", nn.Linear(in_features=224*224*32, out_features=num_classes)),
                    ("Activation_1", nn.Softmax(dim=1))
                    ]))

    def forward(self,x):
        
        out = self.ConvBlock_0(x)
        
        return out
