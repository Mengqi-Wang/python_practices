# -*- coding:utf-8 -*-
from Bio import SeqIO
import sys
print(sys.argv)
filename = sys.argv[0] #sys.argv[0]输出当前运行的py脚本文件，在linux上运行时sys.argv[1]则输出输入文件
filename = filename.split('/')[-1]
record_iterator = SeqIO.parse('011.fasta', 'fasta')
first_record = record_iterator.__next__()
longest_length = len(first_record.seq)
shortest_length = len(first_record.seq)
seq_count = 0
base_total = 0
GC_total = 0
for record in SeqIO.parse('011.fasta', 'fasta'):
    seq_count = seq_count + 1
    base_total = base_total + len(record.seq)
    GC_total = GC_total + record.seq.count('G') + record.seq.count('C')
    if len(record.seq) > longest_length:
        longest_length = len(record.seq)
    if len(record.seq) < shortest_length:
        shortest_length = len(record.seq)
ave_base = base_total/seq_count
out_put = '文件名为： {}\n' \
          '文件共包含碱基数：{}\n' \
          '最长序列碱基数：{}\n' \
          '最短序列碱基数：{}\n' \
          '平均每条序列碱基数：{}\n' \
          '所有序列GC含量：{}'.format('011.fasta', base_total, longest_length, shortest_length, ave_base, GC_total)
with open('011_stat.txt', 'w') as handle:
   handle.write(out_put)