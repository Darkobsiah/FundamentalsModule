number_of_electrons = int(input())
shell_lists = []
for shell in range(1, number_of_electrons + 1):
    maximum_electrons_in_current_shell = 2 * shell ** 2
    if number_of_electrons >= maximum_electrons_in_current_shell:
        shell_lists.append(maximum_electrons_in_current_shell)
        number_of_electrons -= maximum_electrons_in_current_shell
        if number_of_electrons == 0:
            break
    else:
        shell_lists.append(number_of_electrons)
        break

print(shell_lists)