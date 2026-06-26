import os , json

DATA_FILE = "scores.json"

def load_scores():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r",encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_scores(scores):
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(scores,f,ensure_ascii=False)


def add_student(scores,name,score):
    if 0 <= score <= 100:
        scores[name] = score
        return f"{name}: {scores[name]}分已登记"
    return "请输入0-100之间的分数"

def delete_student(scores,name):
    if name in scores:
        scores.pop(name)
        return f"{name}的信息已删除"
    return "未查询到该生信息"

def query_student(scores,name):
    if name in scores:
        return f"{name}的成绩是：{scores[name]}"
    return "未查询到该生信息"

def update_student(scores,name,score):
    if name in scores:
        if 0 <= score <= 100:
            scores[name] = score
            return f"{name}的成绩已修改为{scores[name]}"
        return "请输入0-100之间的分数"
    return "未查询到该生信息"

def get_statistics(scores):
    n = len(scores)
    if n == 0:
        return ["暂无学生数据"]
    
    avg = sum(scores.values())/n
    top = max(scores,key=scores.get)
    failed = [name for name,s in scores.items() if s < 60]

    lines = [
        f"学生总数：{n}\n"
        f"平均分：{avg}\n"
        f"最高分：{top}:{scores[top]}分"
    ]
    if failed:
        lines.append(f"不及格：{','.join(failed)}")
    else:
        lines.append("全部及格")

    return lines

