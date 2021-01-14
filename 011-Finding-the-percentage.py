if __name__ == "__main__":
    n = int(input())
    student_mark={}
    for _ in range(n):
        name, *line=input().split()
        scores = list(map(float, line))
        student_mark[name] = scores
    qury_name=input()
    total_marks = sum(student_mark[qury_name])
    percent = total_marks/3
    print("%.2f"%(percent))