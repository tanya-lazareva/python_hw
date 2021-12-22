import hw4 as class_seq

#СОРТИРОВКА ПОСЛЕДОВАТЕЛЬНОСТЕЙ НК
DNA_ref=input('Введите ДНК-референс: ')
DNA_ref=class_seq.DNA(DNA_ref)

RNA_ref=input('Введите РНК-референс: ')
RNA_ref=class_seq.RNA(RNA_ref)

num_of_seq = int(input('Введите кол-во последовательностей нукл. к-т: '))
collect_RNA={}
collect_DNA={}

for i in range(num_of_seq):
    my_seq=input('Введите последовательность нукл. к-ты: ').upper()
    if 'U' in my_seq:
        my_seq=class_seq.RNA(my_seq)
        print(my_seq.alphabet)
        result_RNA = []
        for index in range(len(RNA_ref.seq)):
            result_RNA.append(int(RNA_ref.seq[index] == my_seq.seq[index]))
            su_R = sum(result_RNA)
        collect_RNA[my_seq.seq] = su_R

    else:
        my_seq = class_seq.DNA(my_seq)
        print(my_seq.alphabet)
        result_DNA = []
        for index in range(len(DNA_ref.seq)):
            result_DNA.append(int(DNA_ref.seq[index] == my_seq.seq[index]))
            su_D=sum(result_DNA)
        collect_DNA[my_seq.seq] = su_D

list_R = list(collect_RNA.items())
list_R.sort(key=lambda k: k[1], reverse=True)
print('Результат сортировки ДНК')
for k in list_R:
    print(k[0])
print(collect_RNA)

list_D=list(collect_DNA.items())
list_D.sort(key=lambda l: l[1], reverse= True)
print('Результат сортировки ДНК')
for l in list_D:
    print(l[0])
print(collect_DNA)

#СОРТИРОВКА ПОСЛЕДОВАТЕЛЬНОСТЕЙ АМИНОКИСЛОТ
Protein_ref=input('Введите референс посл-ти ам-т: ')
Protein_ref=class_seq.Protein(Protein_ref)
alphabet = ['G', 'A', 'V', 'L', 'I', 'M', 'P', 'F', 'W','S', 'T', 'N', 'Q', 'Y',
                'C', 'K', 'R', 'H', 'D', 'E']

num_of_prot = int(input('Введите кол-во последовательностей ам-т: '))
collect_protein={}

for j in range(num_of_prot):
    my_protein=input('Введите последовательность белка: ').upper()
    if (any(am in my_protein for am in alphabet)==False):
        my_protein = input('Введите  повторно последовательность белка: ').upper()
    if any(am in my_protein for am in alphabet):
        my_protein = class_seq.Protein(my_protein)
        result_protein = []
        for index in range(len(Protein_ref.seq)):
            result_protein.append(int(Protein_ref.seq[index] == my_protein.seq[index]))
            su_P = sum(result_protein)
        collect_protein[my_protein.seq] = su_P
list_P=list(collect_protein.items())
list_P.sort(key=lambda m: m[1], reverse= True)
print('Результат сортировки последовательности ам-т')
for m in list_P:
    print(m[0])
print(collect_protein)






