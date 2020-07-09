day009 统计序列ATCG含量
from Bio import SeqIO
with open('009_stat.txt', 'w') as result_handle:
    for record in SeqIO.parse('009.fasta', 'fasta'):
        count_a = 100 * float(record.seq.count('A')) / len(record.seq)
        count_c = 100 * float(record.seq.count('C')) / len(record.seq)
        count_t = 100 * float(record.seq.count('T')) / len(record.seq)
        count_g = 100 * float(record.seq.count('G')) / len(record.seq)
        new_record = '> {} \n A:{}% C:{}% T:{}% G:{}%\n'.format(record.description, count_a, count_c, count_t, count_g)
        result_handle.write(new_record)

#结果保留两位小数
from Bio import SeqIO
with open('009_stat2.txt', 'w') as result_handle:
    for record in SeqIO.parse('009.fasta', 'fasta'):
        count_a = ('%.2f' % (100 * float(record.seq.count('A')) / len(record.seq)))
        count_c = ('%.2f' % (100 * float(record.seq.count('C')) / len(record.seq)))
        count_t = ('%.2f' % (100 * float(record.seq.count('T')) / len(record.seq)))
        count_g = ('%.2f' % (100 * float(record.seq.count('G')) / len(record.seq)))
        new_record = '> {} \n A:{}% C:{}% T:{}% G:{}%\n'.format(record.description, count_a, count_c, count_t, count_g)
        result_handle.write(new_record)