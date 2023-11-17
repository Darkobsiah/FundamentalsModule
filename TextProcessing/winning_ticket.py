# Read User input
tickets = [ticket.strip() for ticket in input().split(', ')]
valid_symbols = ['@', '#', '$']

for ticket in tickets:
    is_winning = False
    is_jackpot = False
    if len(ticket) == 20:
        left_part = ticket[10:]
        right_part = ticket[:10]
        for symbol in valid_symbols:
            counter = 10
            for _ in range(10, 5, -1):
                win_ticket = symbol * _
                if win_ticket in left_part and counter == 10:
                    if win_ticket in right_part:
                        print(f'ticket "{ticket}" - {len(win_ticket)}{symbol} Jackpot!')
                        is_jackpot = True
                        break
                else:
                    if win_ticket in left_part:
                        if win_ticket in right_part:
                            print(f'ticket "{ticket}" - {len(win_ticket)}{symbol}')
                            is_winning = True
            if is_winning or is_jackpot:
                break
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print('invalid ticket')

