from Bio import SeqIO

with open('target_id.txt', 'r') as handle:
    target_id = handle.read()
#print(target_id)
target_list = []
#n = 0
records = SeqIO.parse('019.fasta', 'fasta')
for rer in records:
    if rer.description in target_id:
        target_list.append(rer)
        #n += 1
    else: continue
SeqIO.write(target_list, 'target_id.fasta', 'fasta')
#print(n)