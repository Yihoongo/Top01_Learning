import pandas as pd

# 创建一个简单的学员名单
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, 90, 78, 92],
    'completed_Basics': [True, False, True, True]
}

df = pd.DataFrame(data)

# 目标：选出"分数 > 60" 且 "已完成基础课" 的学员
# 注意：在pandas 里，'and' 要写成 '&'
filter_condition = (df['Score'] > 60) & (df['completed_Basics'] == True)
passed_students = df[filter_condition]

print("--- 筛选后的合格学员 ---")
print(passed_students)