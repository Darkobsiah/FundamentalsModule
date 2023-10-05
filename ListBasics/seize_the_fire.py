fires = input().split('#')
water = int(input())

effort = 0
total_fire = 0
put_out_cells = []

print('Cells:')

for fire in fires:
    args = fire.split(' = ')
    fire_style = args[0]
    amount = int(args[1])
    valid = False
    if water < amount:
        continue

    if fire_style == 'High' and 81 < amount < 125:
        valid = True
    elif fire_style == 'Medium' and 51 < amount < 80:
        valid = True
    elif fire_style == 'Low' and 1 < amount < 50:
        valid = True

    if valid:
        put_out_cells.append(amount)
        water -= amount
        effort += amount * 0.25
        total_fire += amount

for each in put_out_cells:
    print(f' - {each}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')

