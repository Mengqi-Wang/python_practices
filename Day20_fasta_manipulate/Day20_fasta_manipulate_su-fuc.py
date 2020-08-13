from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

records = SeqIO.parse('020.fasta', 'fasta')

operate_method = ["reverse","complement","rna","lower","upper","translate"]

def operate(method,file):
    result = []
    for record in SeqIO.parse(file, 'fasta'):
        if method == "reverse":
            record.seq = record.seq[::-1]
        elif method == "complement":
            record.seq = record.seq.complement()
        elif method == "rna":
            record.seq = record.seq.transcribe()
        elif method == "lower":
            record.seq = record.seq.lower()
        elif method == "upper":
            record.seq = record.seq.upper()
        elif method == "translate":
            record.seq = record.seq.translate()
        result.append(record)
    SeqIO.write(result, '020_'+ method +'.fasta', 'fasta')

if __name__=="__main__":
    for method in operate_method:
        operate(method,'020.fasta')
