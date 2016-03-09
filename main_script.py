# import our functions

from pdbparsingv2 import *
from PDBtoFASTA import *
from get_alignment import *

input_data="2cd0"
# check if input is a file
if (os.path.isfile(input_data)==True):
	protein_name = parse_input(input_data)
else:
	protein_name = input_data
# check if input is a list
if type(protein_name)==list:
	pass
else:
	distancem = get_distancem(protein_name)
	query=PDBtoFASTA('pdb_files/pdb'+ protein_name +'.ent','myseq')
	blast_results = run_BLAST(query)
	clustal_results = run_CLUSTAL(blast_results)
	
