import pandas as pd

df = pd.read_csv("sales.csv")

print("=== 原始数据 ===")
print(df)

# 1️⃣ 先创建销售额（必须提前！）
df['销售额'] = df['价格'] * df['销量']

# 2️⃣ 平均价格
print("\n=== 平均价格 ===")
print(df['价格'].mean())

# 3️⃣ 销量最高
print("\n=== 销量最高的商品 ===")
print(df.sort_values(by='销量', ascending=False).head(1))

# 4️⃣ 最赚钱（多个）
print("\n=== 最赚钱的商品 ===")
print(df[df['销售额'] == df['销售额'].max()])

# 按分类统计销量
print("\n=== 每个分类总销量 ===")
print(df.groupby('分类')['销量'].sum())

# 按分类统计销售额
print("\n=== 每个分类总销售额 ===")
print(df.groupby('分类')['销售额'].sum())

import matplotlib.pyplot as plt

# 分类销售额柱状图
category_sales = df.groupby('分类')['销售额'].sum()

category_sales.plot(kind='bar')

plt.title("各分类销售额")
plt.xlabel("分类")
plt.ylabel("销售额")

plt.show()