#Запрашивает число и возвращает всего его простые делители

numb = int(input("Введите число: "))
count = 0
for i in range(2, numb+1):
    if (numb % i == 0):
     for j in range(2, i):
        if (i % j == 0):
            count = count + 1
     if count == 0:
        print(i)

