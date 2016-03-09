import os
from Bio.PDB import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import colorConverter
import matplotlib as mpl

# Example data

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


distancem = get_distancem("2cd0")


############# http://stackoverflow.com/questions/10127284/overlay-imshow-plots-in-matplotlib


import copy
distancem2=copy.copy(distancem)

contact_map = distancem >15    
contact_map2 = distancem2 >10    # Example data, we'll use here a matrix of MI

# generate the colors for your colormap
color1 = colorConverter.to_rgba('white') # I don't know why this doesn't work..!
color2 = colorConverter.to_rgba('black')

# make the colormaps
cmap1 = mpl.colors.LinearSegmentedColormap.from_list('my_cmap',['red','yellow'],256) #colors[0] at val=0 and colors[1] at val=1. The last mumber is the rgb quantization
cmap2 = mpl.colors.LinearSegmentedColormap.from_list('my_cmap2',[color1,color2],256)

cmap2._init() # create the _lut array, with rgba values

# create your alpha array and fill the colormap with them.
# here it is progressive, but you can create whathever you want
alphas = (np.linspace(1, 0, cmap2.N+3)) # the alphas indicate the transparency
cmap2._lut[:,-1] = alphas

img2 = plt.imshow(np.transpose(contact_map), interpolation='nearest', cmap=cmap1) # Instead of this one we can use one of the already existing color maps too
img3 = plt.imshow(np.transpose(contact_map2), interpolation='nearest', cmap=cmap2)

plt.show()