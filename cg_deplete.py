import sys

# Import sequence from text file and store as a string
with open(sys.argv[1], 'r') as file:
    seq = file.read().replace('\n', '')

# Define dictionary for codons with CGs to preserve GC content (non-synonymous)
cg_deplete_nonsyn = {
    'TCG':'TCC',
    'CCG':'CCC',
    'ACG':'ACC',
    'GCG':'GCC',
    'CGT':'AGG',
    'CGA':'AGG',
    'CGG':'GGG',
    'CGC':'GGC'}

# Define function for observed/expected CpG ratio
def obs_exp_ratio(x):
    obs = x.count('CG')/len(x)
    exp = (x.count('C')/len(x))*(x.count('G')/len(x))
    return obs/exp

# Replace codons containing CGs to preserve GC content
seq_cg_deplete = ''
for i in range(0, len(seq), 3):
    codon = seq[i:i+3]
    if codon in cg_deplete_nonsyn:
        new_codon = cg_deplete_nonsyn[codon]
    else:
        new_codon = codon
    seq_cg_deplete += new_codon

# Check that length of sequence is preserved
if len(seq) == len(seq_cg_deplete):
    print('Length preserved')
else:
    print('Length not preserved')

# Check that GC content of sequence is preserved
if (seq.count('C')+seq.count('G'))/len(seq) == (seq_cg_deplete.count('C')+seq_cg_deplete.count('G'))/len(seq_cg_deplete):
    print('GC content preserved')
else:
    print('GC content not preserved')

# Check CpG ratio of original and CpG-depleted sequence
print("Original CpG ratio:",obs_exp_ratio(seq))
print("New CpG ratio:",obs_exp_ratio(seq_cg_deplete))

# Export CpG-depleted sequence as a text file
cg_deplete_text = open ('seq_cg_deplete.txt', 'w')
n = cg_deplete_text.write(seq_cg_deplete)
cg_deplete_text.close()
