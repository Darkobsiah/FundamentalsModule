student_book = {}
number_of_rows = int(input())

for line in range(number_of_rows):
    student_name = input()
    grade = float(input())
    if student_name not in student_book.keys():
        student_book[student_name] = []
    student_book[student_name].append(grade)


for key, value in student_book.items():
    average = 0
    for v in value:
        average += v
    average = average / len(value)
    if average < 4.5:
        student_book.pop(key)
        break

for key, value in student_book.items():
    average = 0
    for v in value:
        average += v
    average = average / len(value)
    print(f"{key} -> {average:.2f}")