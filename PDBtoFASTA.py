
def PDBtoFASTA(file_pdb,id_pdb):
	fh=open(file_pdb,'r')
	letters = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLU':'E','GLN':'Q','GLY':'G','HIS':'H',
			   'ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
			   'TYR':'Y','VAL':'V'}
	sequence = '>'+ id_pdb+'\n'
	index = 0 # count length FASTA lines
	for line in fh:
		if line.startswith('SEQRES'):
			fields = line.split()
			for i in range(4,len(fields)):
				sequence += letters[fields[i]]
				index += 1
				if index == 80:
					sequence += '\n' 
					index = 0
		if line.startswith('ATOM'):
			break
	fh.close()
	query_file = 'myfile.fasta'
	fout=open(query_file,'w')
	fout.write(sequence.strip())
	return query_file

