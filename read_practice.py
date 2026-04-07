import pandas as pd

# 任务 1：读取刚刚创建的 csv 文件
# 提示：使用 pd.read_csv('文件名')
df = pd.read_csv('my_words.csv')

# 任务 2：筛选出 Is_Mastered 等于 False 的行
# 提示：注意列名的大小写必须完全一致
not_mastered = df[ df['Is_Mastered'] == False ]  

print("--- 还没掌握的单词清单 ---")
print(not_mastered)

# 任务 3：统计一下还有几个单词没掌握
# 提示：使用 len(变量名) 可以得到行数
count = len(not_mastered)
print(f"\n加油！还有 {count} 个硬骨头要啃！")