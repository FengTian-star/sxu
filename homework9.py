import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# 存储路径
save_path1='D:/研究生/数据与知识工程/作业1/9.1.png'
save_path2='D:/研究生/数据与知识工程/作业1/9.2.png'

# 读取数据
data = pd.read_excel('餐饮数据.xlsx')

# 处理缺失值
data = data.dropna(subset=['product1_name', 'product1_comment'])

# 设置中文字体为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 定义评价分类函数
def categorize_rating(rating):
    if '满意' in rating or '惊喜' in rating:
        return '好评'
    elif '失望' in rating or '极差' in rating:
        return '差评'
    else:
        return '中评'

# 计算每个餐馆的总体评价分类数量和订单数量
restaurant_rating_info = []
restaurants = data['title'].unique()
for restaurant in restaurants:
    restaurant_data = data[data['title'] == restaurant]
    good_count = restaurant_data['product1_comment'].apply(categorize_rating).value_counts().get('好评', 0)
    bad_count = restaurant_data['product1_comment'].apply(categorize_rating).value_counts().get('差评', 0)
    neutral_count = restaurant_data['product1_comment'].apply(categorize_rating).value_counts().get('中评', 0)
    order_count = restaurant_data['title'].value_counts().get(restaurant, 0)
    restaurant_rating_info.append({
       '餐馆名称': restaurant,
       '好评数': good_count,
       '差评数': bad_count,
       '中评数': neutral_count,
       '订单数量': order_count
    })

# 将列表转换为DataFrame
restaurant_rating_count = pd.DataFrame(restaurant_rating_info)

# 计算每个餐馆的总体好评率、差评率等指标
restaurant_rating_count['好评率'] = restaurant_rating_count['好评数'] / (restaurant_rating_count['好评数'] + restaurant_rating_count['差评数'] + restaurant_rating_count['中评数'])
restaurant_rating_count['差评率'] = restaurant_rating_count['差评数'] / (restaurant_rating_count['好评数'] + restaurant_rating_count['差评数'] + restaurant_rating_count['中评数'])

# 绘制总体好评率与订单数量的散点图
plt.figure(figsize=(12,8))
plt.scatter(restaurant_rating_count['好评率'], restaurant_rating_count['订单数量'])
plt.xlabel('总体好评率')
plt.ylabel('订单数量')
plt.title('总体好评率对餐馆订单数量的影响')
plt.savefig(save_path1)  # 保存散点图到指定目录，可根据需要修改路径
plt.show()

# 绘制总体差评率与订单数量的散点图
plt.figure(figsize=(12,8))
plt.scatter(restaurant_rating_count['差评率'], restaurant_rating_count['订单数量'])
plt.xlabel('总体差评率')
plt.ylabel('订单数量')
plt.title('总体差评率对餐馆订单数量的影响')
plt.savefig(save_path2)  # 保存散点图到指定目录，可根据需要修改路径
plt.show()

# 计算总体好评率与订单数量的Pearson相关系数
correlation, _ = pearsonr(restaurant_rating_count['好评率'], restaurant_rating_count['订单数量'])
print("总体好评率与订单数量的Pearson相关系数:", correlation)

# 计算总体差评率与订单数量的Pearson相关系数
correlation, _ = pearsonr(restaurant_rating_count['差评率'], restaurant_rating_count['订单数量'])
print("总体差评率与订单数量的Pearson相关系数:", correlation)