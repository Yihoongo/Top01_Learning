import pandas as pd

# 1. 准备数据
data = {
    'Word': ['Frontend', 'Backend', 'Database', 'Middleware', 'Framework'],
    'Difficulty': [3, 5, 8, 9, 6],
    'Is_Mastered': [True, False, False, False, True]
}
df = pd.DataFrame(data)

# --- 你的挑战开始 ---

# 任务 A：找出难度大于 7 的“硬核单词”
# 提示：用 df['Difficulty'] > 7
hard_words = df[ df['Difficulty'] > 7 ]


# 任务 B：找出“难度小于 6” 且 “还没掌握 (False)” 的单词
# 提示：记得用括号 () 和 &
target_words = df[ (df['Difficulty'] < 6) & (df['Is_Mastered'] == False) ]

print("难度大的单词：")
print(hard_words)
print("\n下午要重点复习的单词：")
print(target_words)