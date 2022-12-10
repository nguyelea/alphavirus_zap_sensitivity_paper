import sys

# Import sequence from text file and store as a string
with open(sys.argv[1], 'r') as file:
    seq = file.read().replace('\n', '')

# Define dictionary for codons with possible CGs to preserve GC content (non-synonymous)
cg_enrich_nonsyn = {
    'ACC':'ACG',
    'TCC':'TCG',
    'CCC':'CCG',
    'GCC':'GCG',
    'AGG':'ACG',
    'TGG':'TCG',
    'CGG':'CCG',
    'GGG':'GCG'}

# Define function for observed/expected CpG ratio
def obs_exp_ratio(x):
    obs = x.count('CG')/len(x)
    exp = (x.count('C')/len(x))*(x.count('G')/len(x))
    return obs/exp

# Replace codons to enrich CGs while preserving GC content
seq_cg_enrich = ''
for i in range(0, len(seq), 3):
    codon = seq[i:i+3]
    if codon in cg_enrich_nonsyn:
        new_codon = cg_enrich_nonsyn[codon]
    else:
        new_codon = codon
    seq_cg_enrich += new_codon

# Check that length of sequence is preserved
if len(seq) == len(seq_cg_enrich):
    print('Length preserved')
else:
    print('Length not preserved')

# Check that GC content of sequence is preserved
if (seq.count('C')+seq.count('G'))/len(seq) == (seq_cg_enrich.count('C')+seq_cg_enrich.count('G'))/len(seq_cg_enrich):
    print('GC content preserved')
else:
    print('GC content not preserved')

# Check CpG ratio of original and CpG-enriched sequence
print("Original CpG ratio:",obs_exp_ratio(seq))
print("New CpG ratio:",obs_exp_ratio(seq_cg_enrich))

# Export CpG-enriched sequence as a text file
cg_enrich_text = open ('seq_cg_enrich.txt', 'w')
n = cg_enrich_text.write(seq_cg_enrich)
cg_enrich_text.close()
