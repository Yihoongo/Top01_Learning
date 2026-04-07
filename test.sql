CREATE DATABASE test_db;
USE test_db;
-- 1. 建表 (Create Table)
-- 相当于在 Excel 里新建一个叫“学生表”的工作表
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY AUTO_INCREMENT, -- 自动生成的学号
    name VARCHAR(20) NOT NULL,         -- 姓名
    score INT                          -- 成绩
);

-- 2. 插入数据 (Insert)
-- 往表里手动录入几个学生
INSERT INTO students (name, score) VALUES ('张三', 85);
INSERT INTO students (name, score) VALUES ('李四', 92);
INSERT INTO students (name, score) VALUES ('王五', 78);

-- 3. 查询数据 (Select)
-- 把表里所有的内容都查出来看看
SELECT * FROM students;

SELECT * FROM students 
WHERE score > 80;

SELECT * FROM students 
WHERE name = '王五';

SELECT * FROM students 
WHERE score > 80 AND name LIKE '张%';

