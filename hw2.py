#Выполнение операций над элементами списков, вводимых пользователем
import numpy as np
from operator import sub, mul, truediv

num = int(input('Введите количество списков '))
lists = []

# СОЗДАНИЕ СПИСКОВ
for i in range(num):
    x_i = [i]
    x_i = list(map(int, input('Введите значения элементов списка: ').split()))  # ввод списка пользователем
    lists.append(x_i)

# СОЗДАНИЕ СПИСКОВ ОДИНАКОВОЙ ДЛИНЫ
for i in range(len(lists)):
    while len(lists[i]) < len(max(lists, key=len)):
        lists[i].append(0)
print(lists)
lists =np.array(lists)

#ОПЕРАЦИИ НАД СПИСКАМИ
def sum_list(lists):
    sum_list_result=[sum(x) for x in zip(*lists)]
    return sum_list_result

def arithmetics (lists, func):
  arg1 = lists[0]
  arg2 = lists[1]
  arithmetic = func(arg1,arg2)
  for i in range(2, len(lists)):
    arg1 = arithmetic
    arg2 = lists[i]
    arithmetic = func(arg1,arg2)
  return arithmetic

def deg(lists):
    st_pol=int(input('Введите степень: '))
    for j in range (len(lists)):
        deg_res=[]
        for x in lists:
            for y in x:
                st=y**st_pol
                deg_res.append(st)
    return deg_res

def sq(lists):
    root_pol = int(input('Введите степень корня: '))
    for k in range (len(lists)):
        sq_res=[]
        for x in lists:
            for y in x:
                sqq=y**(1/root_pol)
                sq_res.append(sqq)
    return sq_res

def lg (lists):
    lg_pol = int(input('Введите основание log: '))
    from math import log
    for l in range (len(lists)):
        lg_res=[]
        for x in lists:
            for y in x:
                if (lg_pol !=1 and lg_pol >0) and y>0:
                    lgg=log(y,lg_pol)
                    lg_res.append(lgg)
                if lg_pol<= 0 or lg_pol==1:
                    lg_pol = int(input('Введите основание log: '))
                    lgg = log(y, lg_pol)
                    lg_res.append(lgg)
                if y==0:
                    lg_res.append("NA")
    return lg_res


#ВЫБОР ОПЕРАЦИИ
print('Выберите операцию:\n 1-сложение 2-вычитание 3-умножение 4-деление '
      '5-возведение в степень 6-извлечение корня 7-извлечение логарифма')
choise=int(input('Введите № операции: '))

if choise <1 or choise > 7:
    choise = int(input('Операции не существует. Введите повторно № '))
if choise == 1:
    print(sum_list(lists))
if choise == 2:
    print(arithmetics(lists,sub))
if choise == 3:
    print(arithmetics(lists, mul))
if choise == 4:
    print(arithmetics(lists, truediv))
if choise == 5:
    print(deg(lists))
if choise == 6:
    print(sq(lists))
if choise == 7:
    print(lg(lists))
