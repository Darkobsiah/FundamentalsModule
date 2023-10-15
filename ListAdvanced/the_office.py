def check_employee_happiness():
    happiness_list = list(map(int, input().split()))
    factor = int(input())
    # Find the improved happiness
    improved_happiness = [happiness * factor for happiness in happiness_list]

    # Find the average happiness
    average_happiness = sum(improved_happiness) / len(improved_happiness)

    # Find the count of happy people
    happy_people_count = sum(happier >= average_happiness for happier in improved_happiness)

    # Total count = number of people
    total_count = len(improved_happiness)

    # Message ... if ... else
    message = 'are happy' if happy_people_count >= total_count / 2 else 'are not happy'
    return f'Score: {happy_people_count}/{total_count}. Employees {message}!'
print(check_employee_happiness())

