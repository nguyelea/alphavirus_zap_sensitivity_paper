import sys

# Import sequence from text file and store as a string
with open(sys.argv[1], 'r') as file:
    seq = file.read().replace('\n', '')

# Calculate and print UpA observed/expected ratio
obs = seq.count('UA')/len(seq)
exp = (seq.count('U')/len(seq))*(seq.count('A') / len(seq))
print(obs/exp)
