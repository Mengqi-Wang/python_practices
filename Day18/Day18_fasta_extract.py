
import os
from Bio import SeqIO

n = 0
key = 0
extract_dic = {}
for rec in SeqIO.parse('018.fasta', 'fasta'):
    if key == n // 100:
        extract_dic.setdefault(key + 1, []).append(rec)
    else:
        key = key + 1
        extract_dic.setdefault(key + 1, []).append(rec)
    n = n + 1
#print(len(extract_dic[30]))
result_dict = "Day18_result"
for k, v in extract_dic.items():
    with open(os.path.join(result_dict, '%s.fasta' % (k)), 'w') as handle:
        SeqIO.write(v, handle, 'fasta')
