import re

def returnword():
    return 'собака'

def myword():
    while True:
        temp = input().lower()
        if len(temp) == 6 and not re.search(r'[^а-яА-ЯёЁ]', temp):
            return temp


def cheking(a: str, b: str):
    if a == b:
        return False
    a_list = list(a)
    b_list = list(b)
    letter_in = 0
    letter_true = 0
    result = ''
    for index in range(len(a_list)):
        if a_list[index] in b_list:
            if a_list[index] == b_list[index]:
                letter_true += 1
                result += f'{a_list[index].upper()}'
            else:
                letter_in += 1
                result += f'{a_list[index]}'
        else:
            result += '*'
    return result


if __name__ == '__main__':
    b = returnword()
    a = myword()
    while cheking(a,b) != False:
        c = cheking(a, b)
        print(c)
        a = myword()