import streamlit as st
import pandas as pd
import plotly.express as px  # <--- 就是这一行，新加入的“VIP嘉宾”

# 1. 基础配置
st.set_page_config(page_title="Milk 的万能数据分析助手", layout="wide")

st.title("🚀 Milk 的万能数据分析助手 (Pro版)")
st.markdown("上传表格，开启交互式可视化体验")

# 2. 侧边栏：文件导入
st.sidebar.header("📥 数据中心")
uploaded_file = st.sidebar.file_uploader("拖入你的 sales.csv 或 Excel", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        # 3. 读取数据
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
            # 读取数据后，立即删掉包含 "Unnamed" 的列
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        
        st.success("🎉 数据加载成功！")

        # 4. 核心指标卡片 (增加一点高级感)
        st.subheader("📌 核心指标预览")
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.metric("数据总行数", len(df))
        with col_m2:
            numeric_cols = df.select_dtypes(include=['number']).columns
            if len(numeric_cols) > 0:
                st.metric("平均数值", round(df[numeric_cols[0]].mean(), 2))
        
        st.divider()

        # 5. 可视化实验室
        st.subheader("📊 动态交互分析")
        
        all_columns = df.columns.tolist()
        num_columns = df.select_dtypes(include=['number']).columns.tolist()

        c1, c2, c3 = st.columns(3)
        with c1:
            x_axis = st.selectbox("横坐标 (X轴)", all_columns)
        with c2:
            y_axis = st.selectbox("纵坐标 (Y轴)", num_columns)
        with c3:
            chart_type = st.selectbox("图表样式", ["3D柱状风格", "平滑折线图", "炫彩面积图"])

        # 6. 使用 Plotly 进行高级绘图
        plot_data = df.groupby(x_axis, as_index=False)[y_axis].sum()  # 【核心修改 2】：使用 as_index=False，不再需要后面的 .reset_index()

        if chart_type == "3D柱状风格":
            # barmode="group", color_discrete_sequence 都是为了好看
            fig = px.bar(plot_data, x=x_axis, y=y_axis, color=y_axis, 
                        color_continuous_scale='Viridis',
                        text_auto='.2s', title=f"{x_axis} vs {y_axis} 分析")
        elif chart_type == "平滑折线图":
            fig = px.line(plot_data, x=x_axis, y=y_axis, markers=True, 
                        line_shape="spline", render_mode="svg") # <--- 确保这里是英文括号
        else:
            fig = px.area(plot_data, x=x_axis, y=y_axis, color_discrete_sequence=['#FF4B4B'])

        # 设置 Plotly 图表的主题和布局
        fig.update_layout(hovermode="x unified", template="plotly_white")
        
        # 将图表显示在网页上
        st.plotly_chart(fig, width="stretch")

        # 7. 底层数据查看
        with st.expander("查看原始数据明细"):
            st.dataframe(df, width="stretch")

    except Exception as e:
        st.error(f"分析出错啦：{e}")
else:
    st.info("👋 欢迎Milk ! 请在左侧侧边栏上传一个表格文件开始体验。")