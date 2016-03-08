from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
from Bio import Entrez
import time 
import subprocess

def run_BLAST(query):
	record = SeqIO.read(query, format="fasta")
	print('here')
	fblast=NCBIWWW.qblast('blastp','nr',record.format("fasta")) # non-redundant all db
	fout = open('blast_results.xml','w')
	print('back here')
	fout.write(fblast.read())
	fout.close()
	fread = open('blast_results.xml','r') # read results
	hit_list = list()
	for line in fread:
		if '<Hit_id>gi' in line:
			code = line.split('|')
			hit_list.append(code[1])
	return hit_list

def run_CLUSTAL(hit_list):
	print('back')
	cl_input=open('query.fasta','a')
	cl_input.write('\n')
	fasta_seqs = ''
	#retrieve fasta_seqs
	for ids in hit_list:
		Entrez.email = "nenukab52@gmail.com" # identification needed for access
		handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta", retmode="text")
		time.sleep(1) # avoid sending too many sequences
		sequence = handle.read()
		cl_input.write(sequence)
		'''
		lines=sequence.split('\n')
		fasta_seqs += lines[0]+'\n' # store id
		for i in range(1,len(lines)):
			if not lines[i].startswith('>'): # skip chain identifiers
				fasta_seqs += lines[i]+'\n'
		'''
	#cl_input.write(fasta_seqs)
	#cl_input.write(sequence)
	cl_input.close()
	subprocess.call(['clustalw','-infile=query.fasta','-output=pir','-outfile=query'])

onehitlist=run_BLAST('fastatry.fasta')
run_CLUSTAL(onehitlist)
