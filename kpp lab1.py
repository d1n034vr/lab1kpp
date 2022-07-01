def calculate():
    operation = input('''
Введіть дію:
+ додавання
- віднімання
* множення
/ ділення
''')

    number_1 = int(input('Введіть перше число: '))
    number_2 = int(input('Введіть друге число: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Ви не ввели дійсний оператор, запустіть програму ще раз.')

    again()

def again():
    calc_again = input('''
Ви хочете порахувати ще раз?
Введіть Y якщо так і N якщо ні
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('До побачення.')
    else:
        again()

calculate()