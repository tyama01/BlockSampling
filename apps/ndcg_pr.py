from ndcg import ndcg

pr_original = {}
pr_sample = {}

#with open("../pr_result/amazon_pr_result.txt") as f:
with open("../pr_result/Google_pr_result_cpp.txt") as f:
    for line in f:
        (k, v) = line.split(' ')
        pr_original[int(k)] = float(v)
        
#with open("../pr_result/amazon_pr_top_60_result.txt") as f:
with open("../pr_result/Google_pr_result_py.txt") as f:
    for line in f:
        (k, v) = line.split(' ')
        pr_sample[int(k)] = float(v)
        

rel_true = list(pr_original.values())

#original_keys = list(pr_original.keys())
sample_keys = list(pr_sample.keys())

rel_pred = []

for tmp_key in sample_keys:
    rel_pred.append(pr_original[tmp_key])
    #rel_pred.append(pr_sample[tmp_key])
    
n = len(rel_pred)
x = int(n*0.1)
    
#print(ndcg(rel_true, rel_pred[:x], form="exp"))

rel_true2 = rel_true[:n]

sum = 0

for i in range(n):
    sum += rel_true2[i]
    
for i in range(n):
    rel_true2[i] = rel_true2[i]/ sum

print(ndcg(rel_true, rel_pred, form="exp"))



