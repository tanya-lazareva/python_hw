import random
length=int(input('Введите длину последовательностей: '))
num=int(input('Введите число последовательностей: '))

#генераторы  заданного числа последовательностей заданной длины

def DNA_random(length,num):
    alphabet = ['A', 'T', 'G', 'C']
    print('Последовательности дезоксинуклеотидов:')
    for i in range(num):
        print(''.join(random.choice(alphabet) for j in range(length)))

DNA_random(length,num)

def RNA_random(length,num):
    alphabet = ['A', 'U', 'G', 'C']
    print('Последовательность нуклеотидов ')
    for j in range(num):
        seq = []
        for i in range(length):
            nd=random.choice(alphabet)
            seq.append(nd)
        print(''.join(seq))
RNA_random(length,num)

def protein_random(length,num):
    alphabet = ['G', 'A', 'V', 'L', 'I', 'M', 'P', 'F', 'W', 'S', 'T', 'N', 'Q', 'Y',
                'C', 'K', 'R', 'H', 'D', 'E']
    print('Последовательности аминокислот:')
    for j in range(num):
        seq=[]
        for i in range(length):
            nd = random.choice(alphabet)
            seq.append(nd)
        print(''.join(seq))

protein_random(length,num)


