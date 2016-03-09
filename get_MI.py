import numpy as np

def get_matrix(align_file):
	# number all diferent aminoacids
	protein_letters = 'ACDEFGHIKLMNPQRSTVWY'
	# read alignment into matrix
	fh = open(align_file,'r')
	record = ''
	alignment = list()
	for line in fh:
		line = line.strip()
		if not line.startswith('>') and len(line)>0:
			record += line
			if '*' in line:
				alignment.append(record[0:-1])
				record = ''
	align_mat=[list(align) for align in alignment]
	for row in align_mat:
		print row 

get_matrix('inputautoclu.pir')
# 2D matrix align
			
			
		
