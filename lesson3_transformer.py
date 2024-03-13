import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import math
# pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np
import copy


class Embeddings(nn.Module):

    def __init__(self, d_model, vocab):
        # dmodel:词嵌入的维度
        # vocab:词表的大小
        super(Embeddings, self).__init__()
        # 定义Embedding层
        self.lut = nn.Embedding(vocab, d_model)
        # 将参数传入类中
        self.d_model = d_model

    def forward(self, x):
        # x:代表输入进模型的文本通过词汇映射后的数字张量
        return self.lut(x) * math.sqrt(self.d_model)


# 词嵌入的维度
d_model = 512

# 词表的大小
vocab = 1000

x = Variable(torch.LongTensor([[100, 2, 421, 508], [491, 998, 1, 221]]))

emb = Embeddings(d_model, vocab)
embr = emb(x)
print("embr:", embr)
print(embr.shape)
