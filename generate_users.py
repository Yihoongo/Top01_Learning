import sqlite3
import pandas as pd
import random

conn = sqlite3.connect('learning.db')

# 模拟 51 个用户（ID从 1000 到 1050，对应之前的订单）
user_data = []
names = ['张三', '李四', '王五', '赵六', '钱七', '孙八', '周九', '吴十']
genders = ['男', '女']

for uid in range(1000, 1051):
    user_data.append({
        'user_id': uid,
        'user_name': random.choice(names) + str(uid)[-2:], # 简单拼个名
        'gender': random.choice(genders),
        'age': random.randint(18, 60)
    })

df_users = pd.DataFrame(user_data)
df_users.to_sql('users', conn, if_exists='replace', index=False)

print("✅ 用户表 users 已创建，51位成员已入库！")
conn.close()