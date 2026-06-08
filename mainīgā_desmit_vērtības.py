# programma p60
x = [0] * 10

for number in range(10):
    x[number] = int(input('ievadiet' + str(number + 1) +'.skaitli:'))

    summa = 0
    for number in range(10):
        summa = summa + x[number] # summas aprēķināšanas

        print()
        print(f'ievadīto skaitļu vidēja vērtība ir {summa/10:0.2f}')
        #formatēta izvade ar 2 zīmēm aiz komata