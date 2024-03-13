import torch
import torch.nn as nn
import matplotlib
matplotlib.use('TkAgg')
from torch.autograd import Variable
import math
# pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np
import copy
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super(PositionalEncoding, self).__init__()
        # Create a positional encoding matrix with sinusoidal functions
        position = torch.arange(max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2) * -(math.log(10000.0) / d_model))
        pe = torch.zeros(max_len, d_model)
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + self.pe[:, :x.size(1)]
        return x

# 创建一张15 x 5大小的画布
plt.figure(figsize=(15,5))
#实例化PositionalEncoding类得到pe对象,输入参数是20和8
pe =PositionalEncoding(20,8)
# 然后向pe传入被Variable封装的tensor,这样pe会直接执行forward函数#且这代tensor里的数值都是8,被处理后相当于位置编码张量
y=pe(Variable(torch.zeros(1,100,20)))
# 然后定义画布的横纵坐标,横坐标到188的长度,纵坐标是某一个词汇中的某维特征在不同长度下对应的值# 因为总共有20维之多,我们这里只查看4,5,6,7维的值.
plt.plot(np.arange(180),y[0,:,4:8].data.numpy())
# 在画布上填写维度提示信息
plt.legend(["dim %d"%p for p in [4,5,6,7]])

