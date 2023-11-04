students_records = {
    'Ivan': {'Math': 5, 'Science': 6, 'English': 5},
    'Nikolay': {'Math': 4, 'Science': 6, 'English': 6},
    'Maria': {'Math': 6, 'Science': 6, 'English': 3}
}
counter = 1
for name, value in students_records.items():
    for subject, score in value.items():
        print(f'[{counter}] {subject} - {score}')

    counter += 1