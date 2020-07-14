from Bio import SeqIO
less = []
over = []
for record in SeqIO.parse('012.fasta', 'fasta'):
    if len(record.seq) < 1000:
        less.append(record)
    else:
        over.append(record)
#print(len(less), len(over))
SeqIO.write(less, 'less1000bp.fasta', 'fasta')
SeqIO.write(over, 'over1000bp.fasta', 'fasta')

