import pandas as pd
import matplotlib.pyplot as plt

# 存储路径
save_path='D:/研究生/数据与知识工程/作业1/8'

# 读取数据
data = pd.read_excel('餐饮数据.xlsx')

# 将purchase_time列转换为日期时间格式
data['purchase_time'] = pd.to_datetime(data['purchase_time'])

# 提取星期几的信息
data['weekday'] = data['purchase_time'].dt.weekday

# 筛选出product1_name不为空的数据
filtered_data = data[data['product1_name'].notnull()]

# 按星期几统计订单数量
order_count_by_weekday = data.groupby('weekday')['comment_id'].count().reset_index()
order_count_by_weekday.columns = ['weekday', 'order_count']

# 设置中文字体为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 绘制柱状图
weekday_names = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
plt.bar(weekday_names, order_count_by_weekday['order_count'])
plt.xlabel('星期几')
plt.ylabel('订单数量')
plt.title('星期几对订单数量的影响')
plt.savefig(save_path)  # 保存对比直方图到指定目录，可根据需要修改路径
plt.show()
