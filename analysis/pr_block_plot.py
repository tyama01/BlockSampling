import matplotlib.pyplot as plt
import numpy as np
import sys

block_score = []

with open("analysis/web-Google_cross_block_score_005.txt", encoding='utf-8') as f:
    for line in f.readlines():
        try:
            score = float(line)
        except ValueError as e:
            print(e, file=sys.stderr)
            continue
        
        block_score.append(score)
        

            
arr_block_score = np.array(block_score)

plt.hist(arr_block_score, bins=500)
plt.xlim(left=0)
plt.xlabel("PageRank Block Score")
plt.ylabel("Frequency")

plt.savefig("analysis_data/web-Google/web-Google_cross_block_005.pdf")