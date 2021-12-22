#Запрашивает число и возвращает максимальное простое число меньше заданного

numb = int(input("Введите число: "))
count = 0
for i in range(numb-1, 1,-1):
    for j in range(2, i):
       if (i % j == 0):
         count = count + 1
    if count == 0:
        print(i)
        break
    else:
      count = 0

