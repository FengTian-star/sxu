import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('餐饮数据.xlsx')

# 忽略product1_name中为空的数据
df = df[df['product1_name'].notnull()]

# 统计每个餐馆的评论数量，作为销量衡量
restaurant_sales = df['title'].value_counts().head(10)

# 存储每个餐馆最受欢迎的菜品及其销量
popular_dishes = {}

# 遍历销量前十的餐馆
for restaurant in restaurant_sales.index:
    # 筛选出当前餐馆的菜品数据
    restaurant_df = df[df['title'] == restaurant]
    # 统计每个菜品的出现次数
    dish_counts = restaurant_df['product1_name'].value_counts()
    if not dish_counts.empty:
        # 存储当前餐馆最受欢迎的菜品（出现次数最多的菜品）及其销量
        popular_dishes[restaurant] = (dish_counts.index[0], dish_counts.iloc[0])

# 设置中文字体为黑体，解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘制柱状图
plt.figure(figsize=(12, 12))
bars = []
for i, (restaurant, (dish, count)) in enumerate(popular_dishes.items()):
    bar_container = plt.bar(i, count, label=dish)
    bars.append(bar_container)

# 设置图表标题和坐标轴标签
plt.title('销量前十餐馆中最受欢迎菜品的销量对比')
plt.xlabel('餐馆名称')
plt.ylabel('菜品销量')

# 设置x轴刻度标签
plt.xticks(range(len(popular_dishes)), popular_dishes.keys(), rotation=45)

# 添加图例
plt.legend()

# 在柱子上添加数据标签
for bar_container in bars:
    for bar in bar_container:
        height = bar.get_height()
        plt.annotate(f'{height}',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')

# 存储图表
save_path='D:/研究生/数据与知识工程/作业1/2.png'
plt.savefig(save_path)