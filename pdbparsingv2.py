from Bio.PDB import *
import pylab
import numpy as np
import os.path as os
from Bio import SeqIO

def parse_input(input_data):
	if os.isfile(input_data)==True:
		handle = open(input_data, "rU")
		for record in SeqIO.parse(handle, "fasta") :
			main_function1(record.id)
		
	else:
		main_function1(input_data)
		
def main_function1(protein_name):
	parser = PDBParser()
	pdbl = PDBList() 
	fh=pdbl.retrieve_pdb_file(protein_name) #downloads the pdb file of 2CD0 protein
	structure = parser.get_structure(protein_name,fh) #extrae la inform estruct de la proteina descargada. 2cd0 es trivial.
	mylist2=list()
	
	i=0
	for residue in structure[0].get_residues(): # generator
		tag1=residue.get_full_id()
		mylist=list()
		if tag1[3][0] == " ":
			for residue2 in structure[0].get_residues():
				tag2 = residue2.get_full_id()
				if tag2[3][0]== " ":
					try:
						mylist.append(residue['CA']-residue2['CA'])
					except:
						mylist.append(10000)
			mylist2.append(mylist)
			i+=1
	distancem=np.asarray(mylist2)
	'''
	# Thresholded map
	contact_map = distancem > 15    
	pylab.autumn()
	pylab.imshow(np.transpose(contact_map))
	pylab.show()
	'''
	# Colormap
	pylab.matshow(np.transpose(distancem))
	pylab.colorbar()
	pylab.savefig(protein_name + '.png')
