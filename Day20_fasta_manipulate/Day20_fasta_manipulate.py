from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

reverse = []
records = SeqIO.parse('020.fasta', 'fasta')
records = SeqIO.parse('020.fasta', 'fasta')
for record in records:
    record.seq = record.seq[::-1]
    reverse.append(record)
SeqIO.write(reverse, '020_reverse.fasta', 'fasta')

complement = []
records = SeqIO.parse('020.fasta', 'fasta')
for record in records:
    record.seq = record.seq.complement()
    complement.append(record)
SeqIO.write(complement, '020_complement.fasta', 'fasta')

rna = []
records = SeqIO.parse('020.fasta', 'fasta')
for record in records:
    record.seq = record.seq.transcribe()
    rna.append(record)
SeqIO.write(rna, '020_RNA.fasta', 'fasta')

lower = []
records = SeqIO.parse('020.fasta', 'fasta')
for record in records:
    record.seq = record.seq.lower()
    lower.append(record)
SeqIO.write(lower, '020_lower.fasta', 'fasta')

upper = []
records = SeqIO.parse('020.fasta', 'fasta')
for record in records:
    record.seq = record.seq.upper()
    upper.append(record)
SeqIO.write(upper, '020_upper.fasta', 'fasta')

translate = []
records = SeqIO.parse('020.fasta', 'fasta')
for record in records:
    record.seq = record.seq.translate()
    translate.append(record)
SeqIO.write(translate, '020_translate.fasta', 'fasta')

