from data import *
from ui import *

scores = load_scores()
print(f"已加载{len(scores)}名学生数据")

while True:
    print_menu()
    choice = input("请输入选项：")

    if choice == "1":
        name = input("姓名：")
        score = float(input("成绩："))
        print(add_student(scores,name,score))

    elif choice == "2":
        print_all_students(scores)

    elif choice == "3":
        name = input("请输入要查询的学生姓名：")
        print(query_student(scores,name))

    elif choice == "4":
        name = input("请输入要修改的学生姓名：")
        score = float(input("请输入要修改的成绩："))
        print(update_student(scores,name,score))

    elif choice == "5":
        name = input("请输入要删除学生的姓名：")
        print(delete_student(scores,name))

    elif choice == "6":
        for line in get_statistics(scores):
            print(line)

    elif choice == "7":
        save_scores(scores)
        print("文件保存成功")

    elif choice == "8":
        break

    else:
        print("请输入1-8")

    print_separator()

print("goodbye!")
