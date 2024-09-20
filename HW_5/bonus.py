# Напишите однострочный генератор словаря,
#  который принимает на вход три списка 
# одинаковой длины: имена str, ставка int, 
# премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа
#  и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии 

def gen_dict(names_list, salaries_list, bonuses_list):
    return {name: salary * (1 + float(bonus.strip('%')) / 100)
             for name, salary, bonus
               in zip(names_list, salaries_list, bonuses_list)}

names = ['Иван', 'Петр', 'Сергей']
salaries = [10000, 15000, 20000]
bonuses = ['10%', '72.5%', '12.545%']

salary_dict = gen_dict(names, salaries, bonuses)
print(salary_dict)