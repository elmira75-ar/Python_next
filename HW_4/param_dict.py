'''Напишите функцию принимающую на вход только ключевые параметры
и возвращающую словарь, где ключ — значение переданного аргумента,
а значение — имя аргумента. Если ключ не хешируем, используйте
его строковое представление.'''

# ключом может быть только неизменяемый (хэш-й) объект
# список, словарь ключом быть не может

def create_dict(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        try:
            result_dict[value] = key
        except:
            result_dict[str(value)] = key 
    return result_dict

print(create_dict(name = 'El',age = 48, other = [10, 20]))

