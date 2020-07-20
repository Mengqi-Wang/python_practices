from Bio import SeqIO
truncated = []
for record in SeqIO.parse('016.fasta', 'fasta'):
    n = len(record.seq) // 3
    start = n
    end = len(record.seq) - int(n)
    record.seq = record.seq[int(start): int(end)]
    truncated.append(record)
SeqIO.write(truncated, 'truncated.fasta', 'fasta')