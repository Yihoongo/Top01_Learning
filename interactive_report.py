import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. 解决 Mac 绘图中文乱码问题
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def run_report():
    # 连接数据库
    conn = sqlite3.connect('learning.db')
    
    print("--- 欢迎使用全栈数据点单器 ---")
    # 2. 接收用户输入
    target_city = input("请输入你想查询的城市（例如：上海、北京、广州）：")
    
    # 3. 编写带变量的 SQL
    # 用 f-string 把你输入的城市精准地塞进 WHERE 条件里
    sql = f'''
    SELECT o.category, SUM(o.amount) as total
    FROM orders o
    JOIN users u ON o.user_id = u.user_id
    WHERE o.city = '{target_city}'
    GROUP BY o.category
    '''
    
    try:
        # 4. 用 Pandas 执行并读取数据
        df = pd.read_sql_query(sql, conn)
        
        if df.empty:
            print(f"❌ 抱歉，数据库里找不到 '{target_city}' 的数据，请检查错别字。")
        else:
            print(f"✅ 已找到 {target_city} 的数据：")
            print(df)
            
        # 5. 生成饼图可视化
        plt.figure(figsize=(8, 6))
        # 把 labels=df['gender'] 改成 labels=df['category']
        plt.pie(df['total'], labels=df['category'], autopct='%1.1f%%', startangle=140)
        plt.title(f"{target_city} 各品类消费金额占比")
        plt.show()
            
    except Exception as e:
        print(f"程序运行出错了：{e}")
    finally:
        conn.close()

if __name__ == "__main__":
    run_report()