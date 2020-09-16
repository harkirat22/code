if __name__ == '__main__':
    n = int(input("Enter the number of students: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("enter name and marks (Like: Harry 30 40 50): " ).split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input("Enter the student name: ")
    sum = 0
    for each in student_marks.get(query_name):
        print(each)
        sum += each

    average = sum/len(student_marks.get(query_name))
    print(round(average,2))