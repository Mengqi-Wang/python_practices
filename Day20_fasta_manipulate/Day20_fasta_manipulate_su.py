from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from collections import defaultdict

records_dic = defaultdict(list)

records = SeqIO.parse('020.fasta', 'fasta')

for record in records:
    reverse_rec = complement_rec = rna_rec = lower_rec = upper_rec = translate_rec = record
    reverse_rec.seq = reverse_rec.seq[::-1]
    records_dic['reverse'].append(reverse_rec)
    complement_rec.seq = complement_rec.seq.complement()
    records_dic['complement'].append(complement_rec)
    rna_rec.seq = rna_rec.seq.transcribe()
    records_dic['rna'].append(rna_rec)
    lower_rec.seq = lower_rec.seq.lower()
    records_dic['lower'].append(lower_rec)
    upper_rec.seq = upper_rec.seq.upper()
    records_dic['upper'].append(upper_rec)
    translate_rec.seq = translate_rec.seq.translate()
    records_dic['translate'].append(translate_rec)
    
for k,v in records_dic.items():
    SeqIO.write(v, '020_'+ k +'.fasta', 'fasta')


