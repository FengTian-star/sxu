import pandas as pd
import matplotlib.pyplot as plt

# 存储路径
save_path='D:/研究生/数据与知识工程/作业1/7'

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

# 提取订单时间的小时信息
data['order_hour'] = data['purchase_time'].dt.hour

# 按小时统计订单数量和平均配送时间
hourly_data = data.groupby('order_hour').agg({'comment_id': 'count', 'delivery_time':'mean'})
hourly_data.columns = ['order_count', 'avg_delivery_time']

# 绘制订单数量和平均配送时间随时间变化的折线图并保存
plt.plot(hourly_data.index, hourly_data['order_count'], label='订单数量')
plt.plot(hourly_data.index, hourly_data['avg_delivery_time'], label='平均配送时间')
plt.xlabel('订单时间（小时）')
plt.ylabel('数量/分钟')
plt.title('订单数量与平均配送时间随时间变化关系')
plt.legend()
plt.savefig(save_path)  # 保存折线图到指定目录，可根据需要修改路径
plt.show()