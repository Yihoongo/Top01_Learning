import sqlite3
import pandas as pd

# 1. 建立连接（就像拨通数据库的电话）
conn = sqlite3.connect('learning.db')

# 2. 准备一条 SQL 指令：创建一张名为 'tasks" 的表
# 这张表有两列：任务名称 （task_name） 和 状态（status）
sql_create_table = '''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    status TEXT
);
'''

# 3. 执行指令并保存
conn.execute(sql_create_table)
conn.execute("INSERT INTO tasks (task_name, status) VALUES ('安装DBeaver', '已完成')")
conn.execute("INSERT INTO tasks (task_name, status) VALUES ('运行 Python SQL 脚本', '进行中')")
conn.commit()

# 4. 用Pandas 把结果读出来验证一下
df = pd.read_sql_query("SELECT * FROM tasks", conn)
print("--- 数据库读取成功！内容如下 ---")
print(df)

conn.close()