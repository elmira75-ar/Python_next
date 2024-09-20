# В модуль с проверкой даты добавьте возможность запуска
#  в терминале с передачей даты на проверку.

from sys import argv

def _is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def date_is_true(date):
    d, m, y = list(map(int, date.split('.')))
    check_days = {
        1:31,
        2:29 if _is_leap(y) else 28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }

    max_day = check_days.get(m)
    if not max_day or(y > 9999 or y < 1) or (d > max_day or d < 1):
        return False
    else:
        return True
    

if __name__=='__main__':    
    
    print(date_is_true(argv[1]))
    # print(argv)

# C:\Users\elmir\OneDrive\Desktop\GB\Python\HW_6>python real_date.py 01.01.32024
# False