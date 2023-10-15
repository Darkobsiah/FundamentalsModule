def check_employee_happiness():
    happiness_list = list(map(int, input().split()))
    happiness_factor = int(input())

    improved_happiness = [happiness * happiness_factor for happiness in happiness_list]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_count = sum(happiness >= average_happiness for happiness in improved_happiness)
    total_count = len(improved_happiness)

    if happy_count >= total_count / 2:
        message = 'are happy'
    else:
        message = 'are not happy'
    return f'Score: {happy_count}/6. Employees {message}!'

print(check_employee_happiness())

