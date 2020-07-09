#Day 008 统计008.fasta文件每条序列长度，保存在新文件中，文件名称为008_length.txt

from Bio import SeqIO
with open('008_length.txt', 'w') as handle:
    for record in SeqIO.parse('008.fasta', 'fasta'):
        new_record = '> {} \n length: {}bp \n'.format(record.description, len(record.seq))
        handle.write(new_record)