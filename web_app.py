import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. 基础配置
st.set_page_config(page_title="万能数据分析助手", layout="wide")
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

st.title("🛠️ Yihoon 的万能数据分析助手")
st.markdown("上传任意 Excel 或 CSV 文件，瞬间获取可视化报告")

# 2. 侧边栏：文件上传插件
st.sidebar.header("数据导入")
uploaded_file = st.sidebar.file_uploader("选择你的办公表格", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # 3. 自动识别格式并读取
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success("✅ 文件上传成功！")

        # 4. 数据概览
        col1, col2 = st.columns([1, 2])
        with col1:
            st.subheader("数据统计摘要")
            st.write(df.describe()) # 自动算出平均值、最大最小值等
        
        with col2:
            st.subheader("原始数据预览")
            st.dataframe(df.head(10)) # 只看前10行

        # 5. 动态图表（全栈黑科技：让用户自己选画什么图）
        st.markdown("---")
        st.subheader("📈 自定义可视化分析")
        
        all_columns = df.columns.tolist()
        x_axis = st.selectbox("请选择横坐标 (X轴)", all_columns)
        y_axis = st.selectbox("请选择纵坐标 (Y轴)", all_columns)
        
        if st.button("生成分析图表"):
            fig, ax = plt.subplots(figsize=(10, 4))
            # 自动根据数据画柱状图
            df.groupby(x_axis)[y_axis].sum().plot(kind='bar', ax=ax, color='#4A90E2')
            plt.xticks(rotation=45)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"解析文件出错：{e}")

else:
    st.info("💡 请在左侧上传一个表格文件（例如 sales.csv）来开始你的分析。")