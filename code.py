from Bio import SeqIO
DNA_seqs = [(seq_record.seq) for seq_record in SeqIO.parse("test.fasta", "fasta")]
DNA_seq_ID = [(seq_record.id) for seq_record in SeqIO.parse("test.fasta", "fasta")]
Length = [len(seq_record.seq) for seq_record in SeqIO.parse("test.fasta", "fasta")]
DNA_IDs = ([i for i in DNA_seq_ID[0:]])
DNA_seq = ([i for i in DNA_seqs[0:]])
A = [i.count("A") for i in DNA_seq]
T = [i.count("T") for i in DNA_seq]
G = [i.count("G") for i in DNA_seq]
C = [i.count("C") for i in DNA_seq]
CG = [i.count("CG") for i in DNA_seq]
AllNul_dict = {"A":A, "T":T, "C":C, "G":G, "CG":CG, "seq_id":DNA_IDs, "Length":Length}
import pandas as pd
df = pd.DataFrame(AllNul_dict)
df["CpG"] = df.CG
df["C_G"] = (df.C*df.G)
df ["CpG_OE"] = (df.CpG*df.Length)/(df["C_G"])
df.to_csv("CpG_oe.csv")
df = pd.read_csv("CpG_oe.csv")
df.inplace = True
print(df)
