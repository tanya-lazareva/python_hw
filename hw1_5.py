#последовательность Фибоначчи

numb = int(input('Введите число: '))
count = 0
count1 = 0
n=2

for i in range(numb, 1, -1):
    for j in range(2, i):
        if (i % j == 0):
            count = count + 1
    if count == 0:
        print(i)
        fib1 = i
        fib2 = i
        fib = [fib1,fib2]
        while n<=14:
            fibn = fib1+fib2
            fib1=fib2
            fib2=fibn
            list.append(fib, fibn)
            n=n+1
        print(fib)
        break
    else:
        count=0





