import sqlite3
import pandas as pd

# 1. 连接数据库
conn = sqlite3.connect('learning.db')

# 2. 准备好你刚才在 DBeaver 里调通的 SQL
# 用 三引号 ''' 可以让你在 Python 里像在 DBeaver 一样换行写 SQL
sql_query = '''
SELECT category, COUNT(*) AS order_count
FROM orders
GROUP BY category
ORDER BY order_count DESC;
'''

# 3. 祭出全栈分析神器：Pandas
# pd.read_sql_query 这一行直接完成了：执行SQL + 抓取数据 + 转换成表格
df = pd.read_sql_query(sql_query, conn)

import matplotlib.pyplot as plt

# 专门解决 Mac 绘图中文乱码问题
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] 
plt.rcParams['axes.unicode_minus'] = False

# 让 Pandas 直接帮你画个条形图
df.plot(kind='bar', x='category', y='order_count', color='skyblue')
plt.title('Category Sales Count')
plt.show()

# 4. 展示结果
print("📊 自动生成的品类分析报表：")
print(df)

# 5. 关闭连接
conn.close()