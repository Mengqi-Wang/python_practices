#Day1
from Bio import SeqIO
with open('name.txt', 'w') as handle:
    for seq_record in SeqIO.parse('002.fasta', 'fasta'):
        handle.write(seq_record.id + '\n')

'''
record_iter = SeqIO.parse('002.fasta', 'fasta')
first_record = next(record_iter)
print(first_record)
'''

# Day2
from Bio import SeqIO
with open('description.txt', 'w') as handle:
    for seq_record in SeqIO.parse('002.fasta', 'fasta'):
        handle.write(seq_record.description + '\n')

