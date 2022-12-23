These scripts are used in the preprint  "Alphavirus evasion of zinc finger antiviral protein (ZAP) correlates with CpG suppression in a specific viral nsP2 gene sequence." All scripts take RNA sequences as input in text file format. The input sequences must be all uppercase.

## CpG content sliding window calculator (cg_sliding_window.py)
Takes a sequence input as a text file and calculates CpG content (observed/expected) over 500-bp sliding windows with a 250-bp step size. Results of analysis are exported in csv format.

## CpG-depleted sequence generator (cg_deplete.py)
Takes a sequence input as a text file and depletes CpG content non-synonymously while preserving overall GC content. Resulting CpG-depleted sequence is exported as a text file.

## CpG-enriched sequence generator (cg_enrich.py)
Takes a sequence input as a text file and enriches CpG content non-synonymously while preserving overall GC content. Resulting CpG-enriched sequence is exported as a text file.

## UpA content calculator (ua_obs_exp.py)
Takes a sequence input as a text file and returns the UpA content (observed/expected) of that sequence.
