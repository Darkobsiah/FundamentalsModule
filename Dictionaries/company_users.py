company_info = {}

while True:
    command = input()

    if command == "End":
        break

    company, employee_id = command.split(" -> ")
    if company not in company_info:
        company_info[company] = []
    if employee_id not in company_info[company]:
        company_info[company].append(employee_id)


for name, students in company_info.items():
    print(f"{name}")
    for student in students:
        print(f"-- {student}")