# Initialise a dictionary to store the data
data = {}

# Read User input
n = int(input())
for _ in range(n):
    name, HP, MP = input().split()
    data[name] = {'HP': HP, 'MP': MP}

print(data)
# Initialise a while loop
while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    action = command[0]

    # max MP(mana) - 200 ; max HP - 100;
    if action == 'CastSpell':
        hero, MP_needed, spell_name = command[1], command[2], command[3]
        if data[hero]['MP'] >= int(MP_needed):
            data[hero]['MP'] -= int(MP_needed)
            print(f"{data[hero]} has successfully cast {spell_name} and now has {data[hero]['MP']} MP!")
        else:
            print(f"{data[hero]} does not have enough MP to cast {spell_name}!")

    elif action == 'TakeDamage':
        pass
    elif action == 'Recharge':
        pass
    elif action == 'Heal':
        pass