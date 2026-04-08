import sqlite3
import pandas as pd
import random
from datetime import datetime, timedelta

conn = sqlite3.connect('learning.db')

# 模拟数据：用户ID, 城市, 金额, 类别, 订单时间
cities = ['北京', '上海', '广州', '深圳', '杭州', '成都']
categories = ['家电', '书籍', '服装', '食品', '数码']

data = []
for i in range(1, 101):
    data.append({
        'order_id': 2026000 + i,
        'user_id': random.randint(1000, 1050),
        'city': random.choice(cities),
        'amount': round(random.uniform(10, 2000), 2),
        'category': random.choice(categories),
        'order_date': (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d')
    })

df = pd.DataFrame(data)
df.to_sql('orders', conn, if_exists='replace', index=False)
print("✅ 100条模拟订单已注入 orders 表！")
conn.close()