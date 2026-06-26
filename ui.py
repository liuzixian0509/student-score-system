def print_menu():
    print("\n==== 学生成绩管理系统 ====")
    print("1. 添加学生    2. 查看学生")
    print("3. 查询成绩    4. 修改成绩")
    print("5. 删除学生    6. 统计信息")
    print("7. 保存到文件  8. 退出")

def print_separator():
    print("------------------------")

def print_all_students(scores):
    if len(scores) == 0:
        print("暂无学生数据")
    else:
        for name , score in scores.items():
            print(f"{name}:{score}")
