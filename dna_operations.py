dna_rules = {
        1: {'00': 'A', '01': 'G', '10': 'C', '11': 'T'},
        2: {'00': 'A', '01': 'C', '10': 'G', '11': 'T'},
        3: {'00': 'T', '01': 'G', '10': 'C', '11': 'A'},
        4: {'00': 'T', '01': 'C', '10': 'G', '11': 'A'},
        5: {'00': 'C', '01': 'T', '10': 'A', '11': 'G'},
        6: {'00': 'C', '01': 'A', '10': 'T', '11': 'G'},
        7: {'00': 'G', '01': 'T', '10': 'A', '11': 'C'},
        8: {'00': 'G', '01': 'A', '10': 'T', '11': 'C'}
    }

dna_rules_reversed = {
        1: {'A': '00', 'G': '01', 'C': '10', 'T': '11'},
        2: {'A': '00', 'C': '01', 'G': '10', 'T': '11'},
        3: {'T': '00', 'G': '01', 'C': '10', 'A': '11'},
        4: {'T': '00', 'C': '01', 'G': '10', 'A': '11'},
        5: {'C': '00', 'T': '01', 'A': '10', 'G': '11'},
        6: {'C': '00', 'A': '01', 'T': '10', 'G': '11'},
        7: {'G': '00', 'T': '01', 'A': '10', 'C': '11'},
        8: {'G': '00', 'A': '01', 'T': '10', 'C': '11'}
    }

dna_xor_table = {
            'A': {'A': 'A', 'T': 'T', 'C': 'C', 'G': 'G'},
            'T': {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'},
            'C': {'A': 'C', 'T': 'G', 'C': 'A', 'G': 'T'},
            'G': {'A': 'G', 'T': 'C', 'C': 'T', 'G': 'A'}
        }

def dna_encode(bits: str, rule: int) -> str:
    dna_sequence = []

    for i in range(0, len(bits), 2):
       bit_pair = bits[i:i+2]
       nucleotide = dna_rules[rule][bit_pair]
       dna_sequence.append(nucleotide)

    return "".join(dna_sequence)

def dna_decode(dna_sequence:str , rule: int) -> str:
    binary_data = []
    
    for nucleotide in dna_sequence:
      bit_pair = dna_rules_reversed[rule][nucleotide]
      binary_data.append(bit_pair)

    return "".join(binary_data)

def dna_xor(dna1: str, dna2: str) -> str:
  dna_cipher = []

  for i in range(len(dna1)):
    dna_xor = dna_xor_table[dna1[i]][dna2[i]]
    dna_cipher.append(dna_xor)

  return "".join(dna_cipher)