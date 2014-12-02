#reading rna codons and translating them into proteins very slow

map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
 
codon_string = "AUGGUGCAGGUAUACGGUCGUACUAUACUGUUGCGGCUUCCCAACUCUAGGCCAAGACAUAUUAGGCAAUUGCGUAAAUCUAAGGGUUCCAAGAAAGCAAGCUUACAACUUUGGGAAACGUGUUUGCUAAGCACAGCGUCACUAGUAUCCUCUGUCGAGCGUUACUUCUGGCUGAGACUACCUACAUCUAGUCGCCGCCUAUCUACUUGCUACCUCAAUAACGACUCCGACCUCAAAAAUGCCUUUUCGCAUUCAUGCUCCCUGCGUGUUUUACCGAAACAUGCUGAUUGCUCUCAUACUCAAUCUUGCUGUAACCGCUCAGUCAGGGUUUUCGUGGACCUAACUUACCGCAGGUUAAGUACGCUAGUGGGCUCUACAAUGCUUGCCAACUGGCGGUCGCACAAGUCGUUUAGAUGUAAUUCCUACAGACUAUCUUGGGAGGGACAUGCUUUGUUAGAUUCCGUCCAGCUCCCGAAAACAUGUAAGAUGUCUACUGUUCCUUCUGCACCUAUUACAACGUACGUAUGUGUGACCUUUUACUCCUCGAGUCCGUAUUAUAACGACCAAGAAUCAGCUUCACACGACGACAGAGGGCCGCAUCAGUGUAUGUUAGAAACUGCGGGACAUGGAAUGACUGAUGACGUAACGUGGCAUCUUAGCCAAUCUUUACGGAUAUUGAUGUUACCGCGCCCAAAACCCCAGAUUGUGAAAGCGAGUCAAUUUAGGCACUGGUCAUACUUUGGGCGAGAGAUUCUAUCGGACCAUCGCAAUGCGUGGGGAGUAGCAUCAACUGUAGUGCUGGGACCCGUAGGGAUGCACGAUACGAGAAGCAGACCGUCGAAGCCCGAAGCAGGUGACAUACAUGGACGCGGCAAUGGAUGUGCGAUGCCAGGUUGUAACGAAUCAAUUAACAUUCAAGGUCGCGUAGUAACGAGAGAGCCUAACGAGCACCGAGUAGGGUCGGCCCGUUCAUGUGAAACAAGACAUCCACGAUCCGGCCGAAUUUUCCUAAUGUCGGUGCCUCAUAGCGGAACAAUUAUGCAUUAUCUAACGUCAGACCAAACACACCGCCCACGCGGGAGCCACUGGCACGGAGGGGUAGGGUUCCAUCGGGCGGGUCGUCCGCAAACCAACCUUGCUCCGGUAAUCGUAUCUUAUAGGCGGAAAAAACUACUCGCUCUUGACCCUGUGCUCUCUCGUUGUGGUAUCCUGUUGCCAUCUGAUACGGAUACAAUCCUACCAGGUGUACCGCCAGGUCGCAGUGACUUCAUAGAUCGCUACACAUCUAUAACGCUAAGGUGGACGUGUGGCGAGAUAAGACACAUAGUCUCCUUUCCGUCUAUGUCCAUGCCUGCUAAUACGUUUUUCACUACCUUUCCGCUAGGGGGACCGGUUGUGCUGCAAUUAUCUAAGCCUGAGUUUUCGUCGAGAAGGACGCCACGAUGGCUCGCUUGCCCGAUAGGAGGGAGCGGGGUGCCAAUCCUACCUGCGAUGAUAGAGAUGACGCGAAAUCUGCGCAUUCGGACAACUGCUAUAAGAAAGCCCUCAGCCCUCCAGGCCGUGAAGAUGCCUCAACGGGAUGCCAUAGUCGAUCAGCGUGUGGCUCAGCUUAGUGCAGAUUCGAAUUUAAGAACGUUCGGUCUGUCUCCCUCUCUCCGUGUUAAGAAACAUUUCGUGGUCCUGACCCUCUUACUUGUGAUUAUGCCCGGUUAUUUGCUUGGUUAUCGAACAGCAUUUCUUGCGCAAGCUAGUGCACCGGGCAUAAUAGCAGUUGCCUACAGCGAGCUCGGAACACAUCUGAUGCUGAGGCCGAGAAAAGAAAUUAACAAGAAGCUUUUGAAGCAUUAUGGACCGUGUCCAGGAAACUUGAGCUGCUACAGUUUGUUCUACGAAGCGCCGAACAUGGCUACUGAUCUCACUCUGCGGCCACUCCUAUCUCAAUCCAACUCGACACGAAGUUGGACUAGAUGCAUUCUCAUAUUGUGCCGACCGCCGGUCAAGUCAGGGAUUCUCACUUUUAAAAACAAUUGUAAUCACCCUAUAGGGACACCCGCCGGGUAUUUAACGGGGACGAACCAUGUUAAGCUUUGCACUACUCAAAACAAAAUGAGGUCUCGUGGAUAUCGCAUCUGGGUCCUACGUUCGAAGAUCUACGAGAAUGACAAGAAUGUGCGUCGAGCCAUGUUGAUGGGUAAUUGCAACCUCGUGGGACUACCGCAAACCAGCACGAAGGGCAGGAUAAGCCGCAGCACCAAGGCGUAUCUAUUGCGUCUGAACUAUGUAAACACCUUAGAAUCCUGCGUAUGCAUGGUGGGCCGUGAUAUCUGUGCUGAAUGCGGUGACGGUCAUGGCGCUCAUACGAUUAGUUCUGUCUUCUUAUGUACGCGAGUAAAAGGCCCCCCGGGCGCCAUAUGCCGGGCCUAUCCGGGACGAAAUUCCGGUAAUCGGGAUCCGGCUAAUAGAACUAGUAAAGUAGCAGAUGGUCGCUGGCGGGUACGUAGCGUGGACCACACGCAGCCUGUUCACACUGACGUUGCCAAUUACCGAAGAGACGUCCUUCCAGAUCGUCUGGUGAGUCAAGACCAAUGCGGGUCAGACAGUUAUACUACUUUGUGGUGCUGGUGCAAGUCGGUUUCUUUUCGUGGGUCCACCGGACAUUGCAGGUUUAUUAUCAGGUUCGUUGACCCUCACGAAUCAGAUCACGCUUGUUUCUAUUUUAAAGGUGUGAAAGGGUGGAAGCUGGCAAGACGCACGUUUUUUACGAGAAGCAUCUGGAUAAUGUAUAGAGGCGAAACCUUGCCUUUGUUGUCCAUAAUCGCAGGGUCUGUCCGUUCAGGUAGGUGGAUGACGCUCGCGGGCAGUAGAAAGCGGCUCCUGUUGCUCAAGGGUGGGAUAGCGCGGCCUUCGAUGAACUUCGGCUCAGAUCGAAACGAGAGAGGUAUACCUUGUGAUUUUCUUGUAGGUCACUCAUUUCCUGAGGUGAAACGAUUUGGCAAUAAGCUUCCAUUUUUUGACCAACACACAUUCCCUCCUACCCCAAAUAACAGGAGAACACCAUGUUACCUGCUGCACGCCCAGACCAGUAACCUGGUGCCUAAAAAAAUACCGGAUGAGGGCAUUAGCGUCAUCGCAGUAAGAUUGCAGUAUAACGCUGAGGUGGCCCAGCGAGCAUUGGCAGAUACCGACGGCUGUAACUGCAGGAUUUCGACGAUCCUCUGUCUAUUUGUCUUCAAAUUGGCUUAUGUGGGCAAUUCCUUAGAAUCAUCUUUUCGUGUGCACCCGUGUCGUUCCCGCUCUCAGCGAACACGGAACCCCGUUUCCUUUCCGUUACAGAAGGUUGGCCUGAGGCAGGACGUAGCAAUCGAUCGUGCGCGUUUCCUGAAGAGUGGAAGUUGGUUCACCACAUUAACUCGGAUUCGUAAUUGGGAACUUCUAUUAUUCGGGGAAGCGGCGUACGAGGUGGUGUUUUCUCCUGUUUCAUCUUUUAUCUGGCAAUGGGUAAAACUCCAUCCGUACAUAGCUGGCCCAGUUACAACCUUCAUCGUACCUAAACGGAACGAUCGUGUCGAACGGAGAAGCAGAUCUGAGCAUCUGUCAGAGGCUAUAGACGCCGCCGUUGGCCUUGCGGACAUGCGUACGAGGCUUACGUUGUCCCGGACAGGGCAGGCAUACCAGUCCCACUAUACUAUAUCUACCGUCCAUGUCAGUCGAAGCGUUGCUGCAGAGAGGAGGAGGCAGGCUGCGGCGUCCCGGCAUCUACCUAGAACUCGAGUUAAUAAUAAUCCACGCGAGCUUGAUUCGUCGUUGGGCUAUGUAAAGUUCCAACCUAAGCGCAUACAGGUAAGCAAAUACCUGCAGAACGGGAUUGCCUACGGCGAACUAUCUGUUGGCGUGCGAUUGCCAGGCAAUUCAUGCCCAGCAGCAACCUAUCCUCUCAGGGUGUGGGCUUGUCCUCUGUUCCCGUUAACGGGGUUUUACCCUCGCACGCAAGGAGGAAUGUGCCCCAAUGUAAUCAAUAGCCGAUCCGGGACAGUAAACCGGUGGGUAAAACAACACUGCAAGGUUAGCCUGCUCGUAGGUCCCCUGACUUCACGCUUAGCCAGCGGCAUGGACGAAAUGCGAACUGCGGGACAUUCAUUAUGCAACAGCAUGCUUACUGAGUUUGAGGUGAUCUUCCAGCAAAAUAACUGCCAUAUAUCCGCUGCGAUAUUCCCUCUCCACAAGCUGACGAGUCGGACUCCGUUUCUGUUCAACCAUACCCAACCUGGGGCGGAAAACUGCCCUUCGCUGCUUAAGGUGAAACCAAUCCGCCGAUGCCUAGUGACUACUUUGGUAAGGUGCUCUCUAUGGUUGUUAUUACCCGUUUCUUCGCUUGUUAAUUUGGAACUAGUGUUGGGUCACCUCCUCUGGGUUCGCCCUCCAUACCCUCGCGCAAUCAGACCUACGUUGAUAGAGGGCGUAGGGCCACUCCUAAGCAACGGAUAUAACACAGCUGAUUUUCCCGCGAUGUAUUAUCAUCCGAAAGAAGCUUUACAUUUCGUGCAUCUUUCCGUGGCUCACGUCGCAUCAAACUCCACCGCUUACACACAAUUUCAAGCCACGGAGGGAAUGCAAUUGUUGAGGCUUCCGUCAAGAAAUCGAGUUAUCUCUCCGUGCUUCUUAGGUGCAAGGGUUUGGGUAUCCUACCACAUGACUUCGGACUGCGGAGAUUCCAUUCUCUCUAACUGCUUCGUAAUUCCACGCGAUAGUAGAGGACAUAAACGUCCAUUUGCACGUUUCUCUUCGCACCCCAAGGGCAAGCGAAUAAGAUUUACAGACUCCUUUCUCUACUGUGUUGGACUUGAUGAGUGGUUCCCGAAAUGUCCCCUGAGCACACCCCCUCGUCAUGAGCUAGUUACGGAAAAGCGACACAAAUGGGGGCAGUCACUAGCAUCGAUUCUUUCUUUUUCGGCUGUCCAACAGUCCCUUCAUAGCCCGUCGGUGGGUCGCUUUACUCGAACUCGGCGCCCUAACGCCGAUCAGCGGCAGGGUAAUAUGGCCCGUAGUAAAUACAACGCACAUGCUAUCGAUACCGGAUCAUUCUGCAGGAUUGUCCGCUCGAACUCACCGAACUUCAUAAUGGUAGGGUCAGCCAGAUGUUGCCGUUCUGGAGGACGGAGGAGAUACUCUGUGAUUAACUCGGAAGUUUGCCAUGACGGAUCCGUGGUAUUAAGCCGUUUAGUUCACAGGAUUUAUUGUGUGGCCCAUUUCAGGAGUUUCGGUACCCACUUACGGGCUAUCUAUCCUGGCCACCGCCAUGCGUCCCAAUCGACUGCGAACGUUAGUGACGAACAAACAGCCUUUAUUUUACGUAGGGACUGGGAACUUCAUCACAUCCAAAACACGGCGAGGGGGACCUUGCCAGUCAAAACAAUGAGAAUGCCCUUAGAAUUACUGGCACUAUACUAUCCAAUCAUCUUGGAACGAGAUUUCGAUAGUGUGAUUGACGUCAGUCCCAACAACAGUGACUGUAACAGCCAUAAUUACCCCCGUCAACCCGGAUGGGUUGUACUCGCACCCAGGUACGAUCAUGUAACGGUGUCGCGCGCAUUGUUCACAACGGAAUCCGUUGUCGCGUUUAAACUGAAGGUUCGAUCCUGGUGCCAUGCUAUCCCACUAGCAAAGGGUGUCCAGCCGGCCACUUACGACCCAAUUAAGGGUAUUCUCGGCCUCUCGGAGAUCAUCAACCCAGAGAAGCUCAGCGCAGGAUGUGUCAGCGUUAGCCAAGUGUACUGUUUGUGUCAAUCGUACAACUUGACCAUUUCCUACAGGUCAGCAUCGCGUUCGGGUGUUCGAUGCCGACCUCCGCUGACUCAUCUGGGCAUUUUCACUAUUCCUUACUUAUCAACUACUCCCUACGCACCGUGUUCCACUUGGGCCCCGACGGGAAAGCCGUGCGGUCCUUGCCGCCGUAGAACUAACGUCCCGAGCAGAUGCACCGGGUUGCCGCUUGGGUUUUCCCACGGUUUAUUUGGCGAAGACGGGCCCGUACAACCAAAUCAGGCUAUCUUCACUGUCCACUGUCGUGUUAAAGGUACCUAUGGGCGGGGCCAUUGUGAUGAUGACUUCGAUACACCCCGAAAGCCUUUAAACAGACCCGAAUUAUUCAAGUCGCCCUUUGUACAACAGAUAUCUAGCAAUGACAGGCGAUACAUGACCAGACCAUCAUACAGAUUAGGGGAGUGUACCAGUGUAGGCGUGAUUGCCUUCAGGCCAUUGCAAGUGCCAGAAGGGUGCCGACGUGAAAUCCUCCGGAGUCCGACCAGGUAUGCGUCACCUGAGGGGAAGCUUCACUGCGGGACCCGAAGGCCAACGAAAAAGUUUCUCUGUGUCAGCGUGGUGAUCAGACACCCAGUGUGCGAGUACUUACAAUGCUGUUUAGUGGCGAGGCUCCAACACGGCGACAAUAUACUAGGGAGUACCCUUAACCUCAAAACGGACUCUGGGAAGGGUUUACCCGCGGGUUGGGCUCCACACAAACUCCAAACAACUGCACGCUCUUCAAAAAUUGGCGUCACUACUCGUAACUCUUUCAGUAACGAGUUAUAUCCAACUGGUUCUGGAGUUUCCUUAAGACCUUCUGUUAAUCCGGGAUAUACCCAAAUUGCACCAAGCCAUAGUCACAGUUUACAAUUGAACGGGAACAGCAUCGAGCCCUUCGACGUCGAAACACAGGAGUACAGUGGUUGUACGGAUCAGUUAGGUAGCCUUACCUCGCCUAUGCGUACUAUGCAAAUGGAUAUGCGAGCAUUGCAGUCAGUCCAGCGAGUACUAUCGACGCCUAACGGCGAGGGACGUCCGCAGGCGUUGCGGUGCAAGGUUUUUUUAGCUUGUUUAACUGACUCCAGCACUCUAGAGCGAUCAACGCUUGCGUCAUUAUCUAAAAACCAUCCUAGUCGGUAUUUGCUAGUAUCUUUAAUGGAGAUAUAUGCGCCUGGCGCGGCAGCCCAAGCAGGAAUUUUAAUACAUAUCAAUCGGUCUGGAAUUAUACGGGAUCUCUGCUCCGCAGGAAAUGUAAGAAUUAGACACGCAACGCAAAUCCCACACGGUCGUAGCCCCGUUAAUCGCUGUGCUCGAACUGCAACACGUUGGGAAUCAUCGUUGUCUUCGCGAAGUAGUAUUCCUCCUCCACGGUAUUUGGUUUCCUUUAGCCCUUUUUCGACCUGUGUUUGCCCCCAGGGGUGGGCCUCUGAGUCAGUCCGAGCUCGUACAGUCCAUAGACAGCAGGCAAUUUGCGUCCUAACGUAUAGUGUAAGACCCGUGGCCGGGACUUAUAUAGGGCCUGCUGCGACCUACAUCGCCCGUACUCGGCAUCGGCUUCAGUGCGUUUUAGCGAGGAGCAAUUGUUGUAACACCACACACGGCAUGCAAUCAGACGCAUGUAUUUUGGGCCGUGAGAUAAUGCAAGCACAUCUAAGCAUACGAGAAUACCAGCGCUUUUUAUCAGCUAGGGAUUCCAUAUCGAGAUUCUUCAAAAUCUCGGGGGCGUACGCGACGGAGCAGAUUUCGGAACUCUUUACUGAACCCGUGGGGAAGUCUGGCAGCUGUCAUCGACCGCACUUACAAAAUCAUAUAAUUCAUCGUCCACUAAGCCGUAGAUUGGUAGGUGCAUGUCCCAAACCUGCUACAGAACGGACUAGAACCGCCUAUUUCAUUUGCCCUAGGAUCUCAUCGAGGCUGGGACUGGCCUCGUAUUCACCUAGGUGGAGUCUCCAUCCGCGAACCUUUCCCCGGGUGAGGAACAGCGUAAACUCGUCGGCUGAGAACCCAUUCCGCAACGACUCGCACGAAGCAGUCCAGAUUUCUAUCUUAAGUCAAAGUCCUGUCACGGUCGUACAGUGCGAGCUCUCCGAGGGACCAGGGGGCGAUGCUGGGGACUGUGAUAUGUAUCGAAAGGAAUGCUGUAGCCCGGCCUUACCCAAUCGCUCAAGGCGCCCAUGCGGAGAGGCACGUGAGUCUUCUGCGAAUACACACAGAGUGGGUCGGGCCGAAGUGGAAUCAUUGCCAACUGGGGCGGGUGAGUACUCAACGCAGGUAACCAAAUCCGUUCAGUUUUCAGCCGCAGAGAAAGCUCGCCUCUCUUGUACCCACUUGUGUGGAACACUUCGCCUACGCCGACGCCUUCACAGACCGUGUACUCUGUCACGGUUCAGCGUUCGAAAGACUGACUCAAACCUACAUGCUUUUGCGAUCCUGAACAAAUUUACAUUAGGCGCGGCUGACCGAAUGCGCUUGAGCAGCCCGUUUCUAAAGUAUAAUUUUUGCGAGGAAAAAAACAAUGCCGCACAAGGUGGCCUGGUAGUCGAUAAGGCCAGGAAGUUGCUCUGUGGAAACCCUGACGGCGCAUUAACAACAAGAUGGUAUCAUAGUACUGGAAAAUUUCUAACUAUUACGAUGGCUAGGAAUGAGAGCGCUUAG"
 

def pair_list(list_):
    return[list_[i:i+3] for i in xrange(0, len(list_), 3)]
    
codon_list = pair_list(codon_string)
codon_end = len(codon_string)
protein = ""

for c in codon_list:
    for x in map:
        if c == x:
            if map[x] == "STOP":
                continue
            else:
                protein += map[x]