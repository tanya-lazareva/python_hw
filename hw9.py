import random
min=int(input('Введите минимальную длину последовательностей: '))
max=int(input('Введите минимальную длину последовательностей : '))
num=int(input('Введите число последовательностей: '))

#генераторы заданного числа последовательностей произвольной длины в задаваемом диапазоне
def DNA_generator(min, max, num):
    alphabet = ['A', 'T', 'G', 'C']
    print('Последовательности дезоксинуклеотидов:')
    for j in range(num):
        if (min==max):
            length=min
        else:
            length=random.randint(min,max)
        print(''.join(random.choice(alphabet) for i in range(length)))
do_DNA= DNA_generator(min, max, num)

def RNA_generator(min, max, num):
    alphabet = ['A', 'U', 'G', 'C']
    print('Последовательности нуклеотидов:')
    for j in range(num):
        if (min==max):
            length=min
        else:
            length=random.randint(min,max)
        print(''.join(random.choice(alphabet) for i in range(length)))
do_RNA= RNA_generator(min, max, num)

def protein_generator(min, max, num):
    alphabet = ['G', 'A', 'V', 'L', 'I', 'M', 'P', 'F', 'W', 'S', 'T', 'N', 'Q', 'Y',
                'C', 'K', 'R', 'H', 'D', 'E']
    print('Последовательности аминокислот:')
    for j in range(num):
        if (min==max):
            length=min
        else:
            length=random.randint(min,max)
        print(''.join(random.choice(alphabet) for i in range(length)))
do_protein= protein_generator(min, max, num)