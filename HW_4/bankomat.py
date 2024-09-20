'''Возьмите задачу о банкомате из семинара 2. 
Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления 
и снятия средств в список.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третьей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией,
даже ошибочной
Любое действие выводит сумму денег'''

import decimal

decimal.getcontext().prec = 2
MIN_SUM = 50
COMISSION = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_COMISSION = 30
MAX_COMISSION = 600
BONUS = decimal.Decimal(3) / decimal.Decimal(100)
LIMIT = 5_000_000
TAX_RATE = decimal.Decimal(10) / decimal.Decimal(100)


def choice(balance, count, is_flag):
    menu = {
        '1': 'пополнить',
        '2': 'снять',
        '3': 'выйти'
    }
    for k, v in menu.items():
        if k.isdigit():
            print(f'{k}: {v}')
        else:
            print(v)
    
    if balance > LIMIT:
        balance = balance * (1 - TAX_RATE)

    a = input('Введите действие: ')
    if a == '3':
        print(f'Баланс = {balance}')
        is_flag = False
        return balance, is_flag
    elif a == '1':
        balance = give_money(balance)
        count = count + 1
    elif a == '2':
        balance = get_money(balance)
        count = count + 1
    else:
        print('Неверная команда')
        count = count + 1
    
    if count % 3 == 0:
        balance = balance * (1 + BONUS)
    
    print(f'Баланс = {balance}, операции {operations}')
    return balance, is_flag


def get_money(balance):
    money_to_get = int(input('Введите сумму снятия: '))
    percent = money_to_get * COMISSION
    if money_to_get % MIN_SUM == 0:
        if percent < MIN_COMISSION:
            percent = MIN_COMISSION
        elif percent > MAX_COMISSION:
            percent = MAX_COMISSION
        
        if(money_to_get + percent) <= balance:
            operations.append(f'- {money_to_get}')
            return balance - (money_to_get + percent)
        else:
            print('Недостаточно средств')
            return balance
    
    else:
        print('Ошибка! Сумма должна быть кратна 50')
        return balance

def give_money(balance):
    money_to_give = int(input('Введите сумму пополнения: '))
    if money_to_give % MIN_SUM == 0:
        operations.append(f'+ {money_to_give}')
        return balance + money_to_give
    else:
        print('Ошибка! Сумма должна быть кратна 50')
        return balance


operations = []    
balance = 0
count = 0
is_flag = True
while is_flag:
    balance, is_flag = choice(balance, count, is_flag)
