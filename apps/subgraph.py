import networkx as nx
import sys 

G = nx.read_edgelist("../datasets/web-Google_gcc_Gorder.txt", create_using=nx.DiGraph, nodetype=int)
#print(G)

RW_list = []

with open("../node_list/Google_custom3_40_node_list_a1.txt", "r", encoding="utf-8") as fin:
    for line in fin.readlines():
        try:
            num = int(line)
        except ValueError as e:
            print(e, file=sys.stderr)
            
        RW_list.append(num)
        

#size = int(len(ff_list) * 0.7)
H = G.subgraph(RW_list)
#print(H)
#print(nx.is_weakly_connected(H))

nx.write_edgelist(H, "../sampling_datasets/Google_custom3_40_a1.txt", data=False)