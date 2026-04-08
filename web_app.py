import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. 基础配置
st.set_page_config(page_title="万能数据分析助手", layout="wide")
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

st.title("🛠️ Yihoon 的万能数据分析助手")
st.markdown("上传任意 Excel 或 CSV 文件，瞬间获取可视化报告")

# 2. 侧边栏：文件导入
st.sidebar.header("数据导入")
uploaded_file = st.sidebar.file_uploader("选择你的办公表格", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        # 3. 读取数据
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success("✅ 文件上传成功！")

        # 4. 数据概览
        col1, col2 = st.columns([1, 2])
        with col1:
            st.subheader("数据统计摘要")
            st.write(df.describe())
        with col2:
            st.subheader("原始数据预览")
            st.dataframe(df.head(10))

        # --- 这里开始是新加的【视觉实验室】部分 ---
        st.markdown("---")
        st.subheader("📊 自定义可视化分析")
        
        # 自动识别列名（全栈防呆设计）
        all_columns = df.columns.tolist()
        numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

        c1, c2 = st.columns(2)
        with c1:
            x_axis = st.selectbox("请选择横坐标 (X轴)", all_columns)
        with c2:
            y_axis = st.selectbox("请选择纵坐标 (Y轴/数字列)", numeric_columns)

        # 🎨 视觉实验室控件
        st.markdown("##### 🎨 视觉实验室")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            chart_type = st.selectbox("选择图表样式", ["柱状图", "折线图", "面积图"])
        with col_b:
            theme_color = st.color_picker("挑选一个主题色", "#4A90E2")
        with col_c:
            show_data = st.checkbox("显示原始数值表格")

        if st.button("🚀 立即渲染专业报告"):
            fig, ax = plt.subplots(figsize=(10, 4))
            plot_data = df.groupby(x_axis)[y_axis].sum()
            
            if chart_type == "柱状图":
                plot_data.plot(kind='bar', ax=ax, color=theme_color)
            elif chart_type == "折线图":
                plot_data.plot(kind='line', ax=ax, color=theme_color, marker='o')
            elif chart_type == "面积图":
                plot_data.plot(kind='area', ax=ax, color=theme_color, alpha=0.5)
            
            plt.xticks(rotation=45)
            st.pyplot(fig)
            
            if show_data:
                st.table(plot_data)

    except Exception as e:
        st.error(f"解析文件出错：{e}")
else:
    st.info("💡 请在左侧上传一个表格文件（例如 sales.csv）来开始。")