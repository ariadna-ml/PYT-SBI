"""represents the contact map in a network where the node color indicates the AA position and the edge length the distance (lower distance, higher length)"""

from __future__ import division
from Bio.PDB import *
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import os
from pdbparsingv2 import *

# Example
# DistMatrix =np.array([[0,      11.2,    16.2,    10.9],
# 					  [11.2,    0,      17.2,    7.2],
# 					  [16.2,    17.2,    0,      5.1],
# 					  [10.9,    7.2,    5.1,    0] ])



DistMatrix = get_distancem("2cd0")
  



G = nx.Graph()
for i in range(0, DistMatrix.shape[0]):
	for j in range(0, DistMatrix.shape[1]):
		if i > j:
			if DistMatrix[i,j] < 15:
				# G.add_edge(i, j, weight=DistMatrix[i,j], length=DistMatrix[i,j])
				G.add_edge(i,j);
				G[i][j]['weight'] = DistMatrix[i,j]

pos = nx.spring_layout(G)
pos = nx.spring_layout(G,k=0.4,iterations=20) #k=Optimal distance between nodes.


# edge_weight=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])

# pos = nx.spring_layout(G,k=0.35,iterations=20) #k=Optimal distance between nodes.

# nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_weight)
nx.draw_networkx_nodes(G,pos,cmap=plt.get_cmap('jet'), node_color =  G.nodes(), node_size = 100, linewidths="0")
nx.draw_networkx_edges(G,pos,width=0.3,alpha=0.5)
plt.axis('off')
plt.show()




