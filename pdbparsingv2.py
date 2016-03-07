from Bio.PDB import *
import pylab
import numpy as np

if __name__=='__main__':
	fhout=open('outputmatrix.txt','w')
	#1X9L,prot simple de unha soa cadea.
	parser = PDBParser()
	pdbl = PDBList() 
	fh=pdbl.retrieve_pdb_file('2cd0') #downloads the pdb file of 2CD0 protein
	structure = parser.get_structure('2cd0',fh) #extrae la inform estruct de la proteina descargada. 2cd0 es trivial.
	counter=0

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
			print(tag1)
			mylist2.append(mylist)
			i+=1
	print i

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
	pylab.show()
