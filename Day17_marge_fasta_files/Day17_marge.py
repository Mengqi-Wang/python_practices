import os
from Bio import SeqIO
path = "./fasta/"
files = os.listdir(path)
# for filename in files:
#     print(filename)
# with open('marge.fasta', 'w') as merge_handle:
#     for filename in files:
#         with open(path + filename, 'r') as f_handle:
#             for line in f_handle.readlines():
#                 merge_handle.write(line)
merge = []
n = 0
for filename in files:
    for rec in SeqIO.parse(path + filename, 'fasta'):
        n = n + 1
        merge.append(rec)
SeqIO.write(merge, 'merge2.fasta', 'fasta')
print(n)
# from Bio import SeqIO
# n = 0
# for rec in SeqIO.parse('marge.fasta', 'fasta'):
#     n = n + 1
# print(n)
#
# i = 0
# for filename in files:
#     for rec in SeqIO.parse(path + filename, 'fasta'):
#         i = i +1
# print("i:", i)

#linux is easier
#cat * > marge.fasta