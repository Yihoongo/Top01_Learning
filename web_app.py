import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. 网页基础设置
st.set_page_config(page_title="全栈销量大屏", layout="wide")
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] # 解决Mac中文显示

st.title("🚀 全栈工程师的数据指挥中心")
st.markdown("---")

# 2. 侧边栏：交互控件
st.sidebar.header("筛选条件")
# 自动从数据库里捞出所有城市名，做成下拉菜单
conn = sqlite3.connect('learning.db')
city_list = pd.read_sql("SELECT DISTINCT city FROM orders", conn)['city'].tolist()
selected_city = st.sidebar.selectbox("请选择要分析的城市", city_list)

# 3. 核心数据逻辑
sql = f'''
SELECT o.category, SUM(o.amount) as total
FROM orders o
JOIN users u ON o.user_id = u.user_id
WHERE o.city = '{selected_city}'
GROUP BY o.category
'''

df = pd.read_sql(sql, conn)
conn.close()

# 4. 网页布局：分两栏展示
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"📊 {selected_city} 销量明细")
    st.dataframe(df, use_container_width=True) # 展示漂亮的数据表格

with col2:
    st.subheader("📈 品类占比图")
    fig, ax = plt.subplots()
    ax.pie(df['total'], labels=df['category'], autopct='%1.1f%%', startangle=140)
    st.pyplot(fig) # 把图表“发射”到网页上

st.success(f"当前展示的是 {selected_city} 的实时业务数据")