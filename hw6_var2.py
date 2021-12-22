import hw4 as class_seq

#СОРТИРОВКА ДНК
DNA_ref=input('Введите референс посл-ти ДНК: ')
DNA_ref=class_seq.DNA(DNA_ref)

num_of_DNA = int(input('Введите кол-во последовательностей ДНК: '))
collect_DNA={}

for j in range(num_of_DNA):
    my_DNA=input('Введите последовательность ДНК: ').upper()
    my_DNA = class_seq.DNA(my_DNA)
    result_DNA = []
    for index in range(len(DNA_ref.seq)):
        result_DNA.append(int(DNA_ref.seq[index] == my_DNA.seq[index]))
        su_D = sum(result_DNA)
    collect_DNA[my_DNA.seq] = su_D
list_D=list(collect_DNA.items())
list_D.sort(key=lambda l: l[1], reverse= True)
print('Результат сортировки ДНК')
for l in list_D:
    print(l[0])
print(collect_DNA)

#СОРТИРОВКА ПОСЛЕДОВАТЕЛЬНОСТЕЙ АМИНОКИСЛОТ
Protein_ref=input('Введите референс посл-ти ам-т: ')
Protein_ref=class_seq.Protein(Protein_ref)

num_of_prot = int(input('Введите кол-во последовательностей ам-т: '))
collect_protein={}

for j in range(num_of_prot):
    my_protein=input('Введите последовательность белка: ').upper()
    my_protein = input('Введите  повторно последовательность белка: ').upper()
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






