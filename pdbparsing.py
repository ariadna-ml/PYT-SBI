if __name__=='__main__':
	fhout=open('outputmatrix.txt','w')
	from Bio.PDB import *
	import pylab
	import numpy as np
	#1X9L,prot simple de unha soa cadea.
	parser = PDBParser()
	pdbl = PDBList() 
	fh=pdbl.retrieve_pdb_file('1CON') #downloads the pdb file of 2CD0 protein
	structure = parser.get_structure('1CON',fh) #extrae la inform estruct de la proteina descargada. 2cd0 es trivial.
	residues=structure.get_residues() #mirar si separa chains.	
	counter=0

	mylist2=list()
	i=0
	#for model in structure:
	for chain in structure[0]:
		for residue in chain:
			j=0
			mylist=list()
			for residue2 in chain:
				try:
					mylist.append(residue['CA']-residue2['CA'])
				except:
					mylist.append(10000)
				j+=1
				#print j
			mylist2.append(mylist)
			i+=1
	#print i
	distancem=np.asarray(mylist2)
	contact_map = distancem >15    
	pylab.autumn()
	pylab.imshow(np.transpose(contact_map))
	pylab.show()


