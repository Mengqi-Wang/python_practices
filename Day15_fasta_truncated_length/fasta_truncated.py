
from Bio import SeqIO
truncated = []
for record in SeqIO.parse('015.fasta', 'fasta'):
    if len(record.seq) > 100:
        record.seq = record.seq[0 : 100]
        truncated.append(record)
    else:
        truncated.append(record)
SeqIO.write(truncated, 'truncated.fasta', 'fasta')

# print(len(truncated))
# n = 0
# for record in SeqIO.parse('truncated.fasta', 'fasta'):
#     n += 1
#     print(len(record.seq))
# print(n)