import fasttext

# 训练模型
model = fasttext.train_unsupervised('txt/train.txt', model='skipgram')

# 保存模型
model.save_model('model.bin')

# 获取词向量
word_vector = model.get_word_vector("apple")

# 打印词向量
print(word_vector)


