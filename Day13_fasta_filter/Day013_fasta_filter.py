from Bio import SeqIO
# record_iterator = SeqIO.parse('013.fasta', 'fasta')
# first_record = record_iterator.__next__()
# print(first_record.id)
# family_name = first_record.id.split('/')[-1]
# print(family_name)
filter = []
other = []
for record in SeqIO.parse('013.fasta', 'fasta'):
    family_name = record.id.split('/')[-1]
    # print(family_name)
    # if '#' in family_name:
    #     filter.append(record)
    # elif family_name == 'ERV1':
    #     filter.append(record)
    # elif family_name == 'ERVL-MaLR':
    #     filter.append(record)
    # elif family_name == 'Gypsy':
    #     filter.append(record)
    if '#' in family_name or family_name == 'ERV1' or family_name == 'ERVL-MaLR' or family_name == 'Gypsy':
        filter.append(record)
    else:
        other.append(record)
print(len(filter), len(other))
SeqIO.write(filter, 'filter.fasta', 'fasta')
SeqIO.write(other, '013filter.fasta', 'fasta')