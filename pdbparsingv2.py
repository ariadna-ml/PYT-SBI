from Bio.PDB import *
import pylab
import numpy as np
import os
from Bio import SeqIO

def parse_input(input_data):
	if ('.fa' in input_data)==True:
		handle = open(input_data,'r')
		i=0
		protein_name=list()
		for record in SeqIO.parse(handle, "fasta"): 
			pdb_name=(record.id).split("|")
			protein_name.append(pdb_name[0])
			i+=1
		if i==1: # not really a list
			protein_name=str(protein_name)
		return protein_name
		
		
def get_distancem(protein_name):
	d = 'pdb_files'
	if not os.path.exists(d):
		os.makedirs(d)
	parser = PDBParser()
	pdbl = PDBList() 
	fh=pdbl.retrieve_pdb_file(protein_name,obsolete=0,pdir=d) #downloads the pdb file of 2CD0 protein
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
	return distancem

def contactm(distancem,threshold=None):
	if threshold == None:
		# Colormap
		pylab.matshow(np.transpose(distancem))
		pylab.colorbar()
		pylab.savefig(protein_name + '.png')
	else:
		# Thresholded map
		contact_map = distancem > 15    
		pylab.autumn()
		pylab.imshow(np.transpose(contact_map))
		pylab.savefig(protein_name + '_thr.png')
