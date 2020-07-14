# Day10 统计010.fasta文件序列长度和GC含量，保存在新文件中，文件名称为010_stat.txt
from Bio import SeqIO
with open('010_stat.txt', 'w') as result_handle:
    result_handle.write('序列名称, 序列长度, GC含量\n')
    for record in SeqIO.parse('010.fasta', 'fasta'):
        GC_count = ('%.2f' % (100 * float(record.seq.count('G') + record.seq.count('C')) / len(record.seq)))
        new_record = '{}, {}, {}\n'.format(record.description, len(record.seq), GC_count)
        result_handle.write(new_record)