stored_info = {}

while True:
    command = input()
    if command == 'end':
        break
    course, student = command.split(" : ")
    if course not in stored_info:
        stored_info[course] = []
    if student not in course:
        stored_info[course].append(student)

for course, student_list in stored_info.items():
    print(f"{course}: {len(student_list)}")
    for student in student_list:
        print(f"-- {student}")