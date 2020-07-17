# from Bio import SeqIO
# import time
# family_name = []
# other = []
# time_star = time.time()
# print('for1 start')
# for record in SeqIO.parse('014.fasta', 'fasta'):
#     name = record.id.split('/')[-1]
#     if '/' not in record.id:
#         other.append(record)
#     elif name not in family_name:
#         family_name.append(name)
#     else:
#         continue
# print('for1 end')
# SeqIO.write(other, 'other.fasta', 'fasta')
# print(family_name)
# #['ERVL', 'ERV1', 'Gypsy', 'ERVL-MaLR', 'DIRS', 'ERVK', 'ERV-Lenti']
# ERVL = []
# ERV1 = []
# Gypsy = []
# ERVL_MaLR = []
# DIRS = []
# ERVK = []
# ERV_Lenti = []
# print('for2 start')
# for record in SeqIO.parse('014.fasta', 'fasta'):
#     name = record.id.split('/')[-1]
#     if name == 'ERVL':
#         ERVL.append(record)
#     elif name == 'ERV1':
#         ERV1.append(record)
#     elif name == 'Gypsy':
#         Gypsy.append(record)
#     elif name == 'ERVL-MaLR':
#         ERVL_MaLR.append(record)
#     elif name == 'DIRS':
#         DIRS.append(record)
#     elif name == 'ERVK':
#         ERVK.append(record)
#     elif name == 'ERV-Lenti':
#         ERV_Lenti.append(record)
#     else: continue
# print('for2 end')
# family_count = 'ERVL: %d \n' \
#                'ERV1: %d \n' \
#                'Gypsy: %d \n' \
#                'ERVL_MaLR: %d \n' \
#                'DIRS: %d \n' \
#                'ERVK: %d \n' \
#                'ERV_Lenti: %d \n' \
#                'other: %d' % (len(ERVL), len(ERV1), len(Gypsy), len(ERVL_MaLR), len(DIRS), len(ERVK), len(ERV_Lenti), len(other))
# print(family_count)
# print('start writhing file')
# SeqIO.write(ERVL, 'ERVL.fasta', 'fasta')
# SeqIO.write(ERV1, 'ERV1.fasta', 'fasta')
# SeqIO.write(Gypsy, 'Gypsy.fasta', 'fasta')
# SeqIO.write(ERVL_MaLR, 'ERVL-MaLR.fasta', 'fasta')
# SeqIO.write(DIRS, 'DIRS.fasta', 'fasta')
# SeqIO.write(ERVK, 'ERVK.fasta', 'fasta')
# SeqIO.write(ERV_Lenti, 'ERV-Lenti.fasta', 'fasta')
# time_end = time.time()
# print('time cost = ' + str(time_end - time_star))
# sub_family = {}
# for record in SeqIO.parse('014.fasta', 'fasta'):
#     name = record.id.split('/')[-1]
#     sub_family['other'] = []
#     if '/' not in record.id:
#         sub_family['other'].append(record)
#     else:
#         if name not in sub_family.keys():
#             sub_family[name] = []
#             sub_family[name].append(record)
#         else:
#             sub_family[name].append(record)
# print(len(sub_family))
from Bio import SeqIO
sub_family = {}
for record in SeqIO.parse('014.fasta', 'fasta'):
    name = record.id.split('/')[-1]
    if '/' not in record.id:
            sub_family.setdefault('other', []).append(record)
    else:
        sub_family.setdefault(name, []).append(record)
print(len(sub_family))

for k, v in sub_family.items():
    SeqIO.write(v, '%s.fasta' % (k), 'fasta')
