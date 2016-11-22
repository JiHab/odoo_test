import random
import re

x = random.randrange(1, 1000000)
bin_x = bin(x)
# 1)одна строка с регуляркой
re_max = len(max(re.findall(r"1*", bin_x)))
print(re_max)
# 1)циклом.
# ноль докидываем, чтобы поледний раз цикл провалился в else:.
count = 0
count_max = 0
for el in bin_x + '0':
    if el is '1':
        count += 1
    else:
        count_max = count if count_max < count else count_max
        count = 0
print(count_max)

# 2) '.1', '+.5' во флоат преобразуется, значит подходит
list_int = ['.1', '+.5', '2..5', '2', '2,4', '-2.5', '-22.525', '-0002.525000', '+-2', '', '.', '..', 'string']
for el in list_int:
    val = re.match(r"(^[+-]?\d*\.?\d+$)", el.strip())
    print(el + ' —---> ' + str(bool(val)))


# 3)
list_em = ['мфы@sdfsdf.com', 'vasya@gdeto.com', 'vasya@gde-to.ru', 'petya@ne_nayti.com']
for email in list_em:
    em = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_-]+\.[com]+$)", email)
    print(bool(em))

