# DBSCAN聚类算法

from sklearn.cluster import DBSCAN
import pandas as pd

inputfile = 'zscoreddata.xls'  # 待聚类的数据文件
k = 5  # 需要进行的聚类类别数

# 读取数据并进行聚类分析
data = pd.read_excel(inputfile)  # 读取数据

# 调用k-means算法，进行聚类分析
kmodel = DBSCAN()  # n_jobs是并行数，一般等于CPU数较好
kmodel.fit(data)  # 训练模型

print(kmodel)
