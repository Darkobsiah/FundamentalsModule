stored_data = {}

# Read User input
while True:
    command = input()
    if command == 'End':
        break
    company, employee = command.split(" -> ")
    if company not in stored_data:
        stored_data[company] = []
    if employee not in stored_data[company]:
        stored_data[company].append(employee)

for company, employees in stored_data.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")