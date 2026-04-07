# 模拟一名全栈工程师的技能评估
has_python_skills = True
has_sql_skills = False  
english_level = 6  # 假设 1-10 分

# 场景 1：必须同时会python和sql才能入职（end）
can_hire_1 = has_python_skills and has_sql_skills

# 场景 2：会其中一个，且英语大于5分即可（of + end）
can_hire_2 = (has_python_skills or has_sql_skills) and (english_level > 5)

print(f"标准 1 结果：{can_hire_1}")
print(f"标准 2 结果：{can_hire_2}")