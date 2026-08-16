FILE_NAME = "student_system.txt"  

def load_students():
    """尝试读取 student_system.txt，如果文件不存在则返回空列表"""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = []
            for line in f:
                name, score = line.strip().split(",")
                data.append({"name": name, "score": int(score)})
            return data
    except FileNotFoundError:
        print("📂 首次使用，未找到旧数据，已创建新列表。")
        return []


def save_students(data):
    """将列表数据写入 student_system.txt（覆盖写入）"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for s in data:
            f.write(s["name"] + "," + str(s["score"]) + "\n")
    print("💾 数据已保存至文件！")


def main():
    students = load_students()

    while True:
        print("\n--- 📚 学生成绩管理系统 ---")
        print("1. 查看所有学生")
        print("2. 添加学生")
        print("3. 退出并保存")
        
        choice = input("请输入选项(1/2/3): ")

        if choice == "1":
            if not students:
                print("⚠️ 暂无学生数据。")
            else:
                print("\n姓名\t成绩")
                for s in students:
                    print(s["name"] + "\t" + str(s["score"]))

        elif choice == "2":
            name = input("请输入姓名: ")
            try:
                score = int(input("请输入成绩: "))
                students.append({"name": name, "score": score})
                print(f"✅ 已添加 {name}，成绩 {score}。")
            except ValueError:
                print("❌ 成绩请输入有效的数字！")

        elif choice == "3":
            save_students(students)
            print("👋 程序已安全退出，再见！")
            break

        else:
            print("❌ 无效选项，请重新输入。")

if __name__ == "__main__":
    main()
