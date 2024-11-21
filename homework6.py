import pandas as pd
import matplotlib.pyplot as plt

# 存储路径
save_path='D:/研究生/数据与知识工程/作业1/6'

# 读取数据
data = pd.read_excel('餐饮数据.xlsx')

# 将purchase_time列转换为日期时间格式
data['purchase_time'] = pd.to_datetime(data['purchase_time'])

# 提取配送时间（假设service-time列格式为'X分钟送达'，提取其中的分钟数）
data['delivery_time'] = data['service-time'].str.extract(r'(\d+)分钟送达').fillna(0).astype(int)

# 计算配送时间的基本统计信息
print(data['delivery_time'].describe())

# 设置中文字体为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 按餐厅计算平均配送时间
restaurant_delivery_time = data.groupby('title')['delivery_time'].mean().sort_values()

# 输出平均配送时间排名
print(restaurant_delivery_time)

# 选择配送时间最短和最长的餐厅（示例选择前3和后3）
top_3_fastest = restaurant_delivery_time.head(3).index
bottom_3_slowest = restaurant_delivery_time.tail(3).index

# 分别提取这些餐厅的数据
fastest_data = data[data['title'].isin(top_3_fastest)]
slowest_data = data[data['title'].isin(bottom_3_slowest)]

# 绘制对比直方图并保存
plt.hist(fastest_data['delivery_time'], bins=10, alpha=0.5, label='配送较快餐厅', edgecolor='black')
plt.hist(slowest_data['delivery_time'], bins=10, alpha=0.5, label='配送较慢餐厅', edgecolor='black')
plt.xlabel('配送时间（分钟）')
plt.ylabel('订单数量')
plt.title('配送时间对比（最快和最慢餐厅）')
plt.legend()
plt.savefig(save_path)  # 保存对比直方图到指定目录，可根据需要修改路径
plt.show()
