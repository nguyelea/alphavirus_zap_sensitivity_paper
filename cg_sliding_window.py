import sys
import pandas as pd

# Import sequence from text file and store as a string
with open(sys.argv[1], 'r') as file:
    seq = file.read().replace('\n', '')

# Define function to calculate CpG observed/expected ratio
def obs_exp_ratio(seq):
    obs = seq.count('CG')/len(seq)
    exp = (seq.count('C')/len(seq))*(seq.count('G')/len(seq))
    return obs/exp

# Define sliding window iterator with window size 500 and step size 250
def sliding_window_analysis(seq, function, window_size=500,step_size=250):
    for start in range (0, len(seq), step_size):
        end = start + window_size
        if end > len(seq):
            break
        yield start, end, function(seq[start:end])

# Calculate CpG observed/expected ratios over sliding windows and return a dataframe with window start, end, and CpG obs/exp ratio
sliding_window_df = pd.DataFrame()
for start, end, cg in sliding_window_analysis(seq, obs_exp_ratio):
    row = (start, end, cg)
    row_df = pd.DataFrame(row).transpose()
    sliding_window_df = sliding_window_df.append(row_df)
sliding_window_df.rename(columns = {0: "start", 1: "end", 2: "CpG_ratio"})

# Export dataframe as a csv file
sliding_window_df.to_csv('./sliding_window_out.csv', index = False, header = ['window_start', 'window_end', 'CpG_ratio'])
