class Sequence:
    name = 'последовательность'

    def __init__(self, seq):
        self.seq = seq

    def return_name(self):
        return self.name

    def return_sequence(self):
        return self.seq

    def length(self):
        return len(self.seq)


# ЗАДАНИЕ 7 ПОДДЕРЖКА ИНТЕРФЕЙСА SEQUENCE
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.seq):
            raise StopIteration()
        seqq = self.seq[self.index]
        self.index += 1
        return seqq

    def __len__(self):
        return len(self.seq)

    def __getitem__(self,item):
        return self.seq[item]

class DNA(Sequence):
    name='ДНК'
    alphabet = [ 'A', 'T', 'G', 'C']

    def __init__(self,seq):
       self.seq=seq

    def count(self):
        count_list={}
        count_list['A'] = self.seq.count(self.alphabet[0])
        count_list['T'] = self.seq.count(self.alphabet[1])
        count_list['G'] = self.seq.count(self.alphabet[2])
        count_list['C'] = self.seq.count(self.alphabet[3])
        return count_list

# ЗАДАНИЕ 10 (функция принимает алфавит, возвращат функцию пол статистики посл-ти
    def count2(alphabet): #сохр в переменную (ст функцей, можно вызвать переменная(посл-ть))
        def stat(self):
            count_list = {}
            count_list['A'] = self.seq.count(alphabet[0])
            count_list['T'] = self.seq.count(alphabet[1])
            count_list['G'] = self.seq.count(alphabet[2])
            count_list['C'] = self.seq.count(alphabet[3])
            print(count_list)
            return count_list
        return stat

    def mol_mass(self):
        mol_mass= 347*self.seq.count(self.alphabet[0]) +320.2*self.seq.count(self.alphabet[1]) +  \
                  363.2*self.seq.count(self.alphabet[2])  + 323.2*self.seq.count(self.alphabet[3])
        return print('Мол. масса ДНК = ',  round(mol_mass, 3), 'г/моль')

    def complementary (self):
        compl_dict={'A':'T', 'T': 'A', 'G': 'C', 'C':'G'}
        compl_strand = [compl_dict[base] for base in self.seq]
        return print('Комплементарная последовательность: ', compl_strand)

    def transcription(self):
        dna_to_rna_dict={'A':'U', 'T': 'A', 'G': 'C', 'C':'G'}
        transcript = [dna_to_rna_dict[base] for base in self.seq]
        transcript=RNA(transcript)
        return print('Транскрипт: ', transcript.seq)


class RNA(Sequence):
    name = 'РНК'
    alphabet = ['A', 'U', 'G', 'C']

    def __init__(self, seq):
        self.seq = seq

    def count(self):
        count_list = {}
        count_list['A'] = self.seq.count(self.alphabet[0])
        count_list['U'] = self.seq.count(self.alphabet[1])
        count_list['G'] = self.seq.count(self.alphabet[2])
        count_list['C']= self.seq.count(self.alphabet[3])
        return count_list

# ЗАДАНИЕ 10 (функция принимает алфавит, возвращат функцию пол статистики посл-ти
    def count2(alphabet): #сохр в переменную (ст функцей, можно вызвать переменная(посл-ть))
        def stat(self):
            count_list = {}
            count_list['A'] = self.seq.count(alphabet[0])
            count_list['U'] = self.seq.count(alphabet[1])
            count_list['G'] = self.seq.count(alphabet[2])
            count_list['C'] = self.seq.count(alphabet[3])
            print(count_list)
            return count_list
        return stat

    def mol_mass(self):
        mol_mass = 347 * self.seq.count(self.alphabet[0]) + 324.2 * self.seq.count(self.alphabet[1]) + \
                   363.2 * self.seq.count(self.alphabet[2]) + 323.2 * self.seq.count(self.alphabet[3])
        return print('Мол. масса РНК = ', round(mol_mass, 3), 'г/моль')

    def complementary(self):
        compl_rna_dict = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
        compl_rna = [compl_rna_dict[base] for base in self.seq]
        compl_rna=RNA(compl_rna)
        return print('Комплементарная последовательность: ', compl_rna.seq)

    def translation(self):
        rna_codon_dict = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
                     "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
                     "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
                     "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
                     "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
                     "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
                     "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
                     "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
                     "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
                     "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
                     "UAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
                     "UAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
                     "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
                     "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
                     "UGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
                     "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
                     }
        protein_sequence =[]
        protein_start=0
        for i in range(len(self.seq)):
            if (self.seq[i:i + 3] == "AUG"):
                protein_start = i
                for j in range(protein_start, len(self.seq)-2,3):
                    cods=rna_codon_dict[self.seq[j:j + 3]]
                    if (cods == "STOP"):
                        break
                    else:
                        protein_sequence.append(cods)
        protein_sequence=Protein(protein_sequence)
        return print('Последовательность белка:', protein_sequence.seq)

class Protein(Sequence):
    name = 'белок'
    alphabet = ['G', 'A', 'V', 'L', 'I', 'M', 'P', 'F', 'W','S', 'T', 'N', 'Q', 'Y',
                'C', 'K', 'R', 'H', 'D', 'E']

    def __init__(self, seq):
        self.seq = seq

    def count(self):
        count_list={}
        count_list['G']=self.seq.count(self.alphabet[0])
        count_list['A'] =self.seq.count(self.alphabet[1])
        count_list['V']=self.seq.count(self.alphabet[2])
        count_list['L']=self.seq.count(self.alphabet[3])
        count_list['I'] = self.seq.count(self.alphabet[4])
        count_list['M'] = self.seq.count(self.alphabet[5])
        count_list['P'] = self.seq.count(self.alphabet[6])
        count_list['F'] = self.seq.count(self.alphabet[7])
        count_list['W'] = self.seq.count(self.alphabet[8])
        count_list['S'] = self.seq.count(self.alphabet[9])
        count_list['T'] = self.seq.count(self.alphabet[10])
        count_list['N'] = self.seq.count(self.alphabet[11])
        count_list['Q'] = self.seq.count(self.alphabet[12])
        count_list['Y'] = self.seq.count(self.alphabet[13])
        count_list['C'] = self.seq.count(self.alphabet[14])
        count_list['K'] = self.seq.count(self.alphabet[15])
        count_list['R'] = self.seq.count(self.alphabet[16])
        count_list['H'] = self.seq.count(self.alphabet[17])
        count_list['D'] = self.seq.count(self.alphabet[18])
        count_list['E'] = self.seq.count(self.alphabet[19])
        return count_list

# ЗАДАНИЕ 10 (функция принимает алфавит, возвращат функцию пол статистики посл-ти
    def count2(alphabet): #сохр в переменную (ст функцей, можно вызвать переменная(посл-ть))
        def stat(self):
            count_list = {}
            count_list['G'] = self.seq.count(self.alphabet[0])
            count_list['A'] = self.seq.count(self.alphabet[1])
            count_list['V'] = self.seq.count(self.alphabet[2])
            count_list['L'] = self.seq.count(self.alphabet[3])
            count_list['I'] = self.seq.count(self.alphabet[4])
            count_list['M'] = self.seq.count(self.alphabet[5])
            count_list['P'] = self.seq.count(self.alphabet[6])
            count_list['F'] = self.seq.count(self.alphabet[7])
            count_list['W'] = self.seq.count(self.alphabet[8])
            count_list['S'] = self.seq.count(self.alphabet[9])
            count_list['T'] = self.seq.count(self.alphabet[10])
            count_list['N'] = self.seq.count(self.alphabet[11])
            count_list['Q'] = self.seq.count(self.alphabet[12])
            count_list['Y'] = self.seq.count(self.alphabet[13])
            count_list['C'] = self.seq.count(self.alphabet[14])
            count_list['K'] = self.seq.count(self.alphabet[15])
            count_list['R'] = self.seq.count(self.alphabet[16])
            count_list['H'] = self.seq.count(self.alphabet[17])
            count_list['D'] = self.seq.count(self.alphabet[18])
            count_list['E'] = self.seq.count(self.alphabet[19])
            print(count_list)
            return count_list
        return stat

    def mol_mass(self):
        mol_mass= 75*self.seq.count(self.alphabet[0]) + 89*self.seq.count(self.alphabet[1]) + \
                  117.2*self.seq.count(self.alphabet[2]) + 131.2*self.seq.count(self.alphabet[3]) + \
                  131.2*self.seq.count(self.alphabet[4]) + 149.2*self.seq.count(self.alphabet[5]) +\
                  115.1*self.seq.count(self.alphabet[6]) + 165.2*self.seq.count(self.alphabet[7]) + \
                  204.2*self.seq.count(self.alphabet[8]) + 105.9*self.seq.count(self.alphabet[9]) + \
                  119*self.seq.count(self.alphabet[10]) + 132*self.seq.count(self.alphabet[11]) + \
                  146*self.seq.count(self.alphabet[12]) + 181.2*self.seq.count(self.alphabet[13]) +\
                  121.2*self.seq.count(self.alphabet[14]) + 146.2*self.seq.count(self.alphabet[15]) + \
                  174.2*self.seq.count(self.alphabet[16]) + 155.2*self.seq.count(self.alphabet[17]) + \
                  131*self.seq.count(self.alphabet[18])+ 147*self.seq.count(self.alphabet[19])
        return print('Мол. масса белка = ', round(mol_mass, 3), 'Da')














