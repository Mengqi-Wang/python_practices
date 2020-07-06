#Day 04 将004.fasta文件里面所有序列的名称里面的空格替换成下划线“_”，保存在新文件中，文件名称为004_rename.fasta
from Bio import SeqIO
my_record = []
for record in SeqIO.parse('004.fasta', 'fasta'):
    # new_record = record
    # new_record.description = record.description.replace(' ', '_')
    # my_record.append(new_record)
    record.description = record.description.replace(' ', '_')
    my_record.append(record)
SeqIO.write(my_record, '004_rename.fasta', 'fasta')

# record_iter = SeqIO.parse('004.fasta', 'fasta')
# first_record = next(record_iter)
# print(first_record)

with open('1.reg', 'r', encoding='utf-16-le') as handle:
    print(handle.readlines()) #同一行打印
    一行一行逐渐打
    for line in handle:
        print(line)

#Day5 将005.fasta文件里面所有序列名称里面的virus删除，保存在新文件中，文件名称为005_rename.fasta
from Bio import SeqIO
my_record = []
for record in SeqIO.parse('005.fasta', 'fasta'):
    record.description = record.description.lower().replace('virus', '')
    my_record.append(record)
SeqIO.write(my_record, '005_rename.fasta', 'fasta')

with open('005.fasta', 'r') as handle, open('005_rename2.fasta', 'w') as f:
    for line in handle:
        if line.startswith('>') and 'virus' in line.lower():
            line = line.lower().replace('virus', '')  #改变了原序列名称中的大小写
        f.write(line)


with open('005.fasta', 'r') as handle, open('005_rename2.fasta', 'w') as f:
    for line in handle:
        if line.startswith('>') and 'virus' in line.lower():
            index = line.lower().index('virus')
            old_virus = line[index: index + 5]
            line = line.replace(old_virus, '')
            #line = line.replace(line[index: index + 5], '')
        f.write(line)


#Day 6 将006.fasta文件里面所有序列的名称后面加上“NCBI”，保存在新文件中，文件名称为006_rename.fasta
from Bio import SeqIO
my_record = []
for record in SeqIO.parse('006.fasta', 'fasta'):
    record.description = record.description + ' NCBI'
    my_record.append(record)
SeqIO.write(my_record, '006_rename.fasta', 'fasta')


with open('006.fasta', 'r') as handle, open('006_rename2.fasta', 'w') as f:
    for line in handle:
        if line.startswith('>'):
            line = line.strip() + ' NCBI\n'
        f.write(line)


#day 007 将007.fasta文件里面所有序列的名称后面加上序号，保存在新文件中，文件名称为007_rename.fasta

from Bio import SeqIO
my_record = []
n = 1
for record in SeqIO.parse('007.fasta', 'fasta'):
    record.description = record.description + ' ' + str(n)
    my_record.append(record)
    n = n + 1
SeqIO.write(my_record, '007_rename.fasta', 'fasta')

n = 0
with open('007.fasta', 'r') as handle, open('007_rename2.fasta', 'w') as f:
    for line in handle:
        if line.startswith('>'):
            n = n + 1
            line = line.strip() + ' ' + str(n) + '\n'
        f.write(line)