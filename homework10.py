import pandas as pd
import matplotlib.pyplot as plt

# 存储路径
save_path='D:/研究生/数据与知识工程/作业1/10.png'

# 读取数据
data = pd.read_excel('餐饮数据.xlsx')

# 设置中文字体为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 将purchase_time列转换为日期时间格式
data['purchase_time'] = pd.to_datetime(data['purchase_time'])

# 提取日期信息
data['date'] = data['purchase_time'].dt.date

# 清洗service-time列，提取数值部分（假设格式为'X分钟送达'，提取X）
data['service-time'] = data['service-time'].str.extract(r'(\d+)')

# 填充NaN值为0，使用重新赋值方式
data['service-time'] = data['service-time'].fillna(0)

# 转换数据类型为整数
data['service-time'] = data['service-time'].astype(int)

# 计算每个日期的平均配送时间
average_delivery_time = data.groupby('date')['service-time'].mean().reset_index()

# 定义函数判断是否为周末
def is_weekend(date):
    return date.weekday() >= 5

# 添加是否为周末的列
average_delivery_time['is_weekend'] = average_delivery_time['date'].apply(is_weekend)

# 分别计算周末和工作日的平均配送时间
weekend_delivery_time = average_delivery_time[average_delivery_time['is_weekend']]['service-time'].mean()
weekday_delivery_time = average_delivery_time[~average_delivery_time['is_weekend']]['service-time'].mean()

# 绘制日期与平均配送时间的折线图
plt.figure(figsize=(8,6))
plt.plot(average_delivery_time['date'], average_delivery_time['service-time'])
plt.xlabel('日期')
plt.ylabel('平均配送时间（分钟）')
plt.title('日期对配送时间的影响')
plt.xticks(rotation=45)

# 绘制表示周末平均配送时间的横线
plt.axhline(y=weekend_delivery_time, color='r', linestyle='--', label=f'周末平均配送时间: {weekend_delivery_time:.2f}分钟')

# 绘制表示工作日平均配送时间的横线
plt.axhline(y=weekday_delivery_time, color='g', linestyle='--', label=f'工作日平均配送时间: {weekday_delivery_time:.2f}分钟')

plt.legend()  # 显示图例
plt.savefig(save_path)  # 保存散点图到指定目录，可根据需要修改路径
plt.show()