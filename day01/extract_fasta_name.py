from Bio import SeqIO
with open('name.txt', 'w') as handle:
    for seq_record in SeqIO.parse('001.fasta', 'fasta'):
        handle.write(seq_record.id + '\r\n')