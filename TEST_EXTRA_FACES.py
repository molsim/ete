# TO RUN THIS SCRIPT: 
# Create a symbolic link "ete_dev" pointing to the "ete2" dir. 
# Then, execute (within this directory):
# PYTHONPATH=`pwd` python TEST_EXTRA_FACES.py
#

from ete_dev import Tree, faces, layouts
from ete_dev.treeview import drawer
import re
    
def ly(node):
    layouts.basic(node)
    if node == n: 
	faces.add_face_to_node(faces.SequenceFace("aaaaaaaaaaaaaaaaaaaaaaaaiiiiiiiipppppppppppppaaa", "aa"),node, 1, aligned=True)	



t =Tree()
t.populate(10)
A1=faces.SequenceFace("HOLAFRANCOISaaaaaaaaaaaaaaaaaaaaaaaaaaiiiiiiiipppppppppppppaaa", "aa")
A2=faces.SequenceFace("aaaaaaaaaaaaaaaaaaaaaaaaaaaaiiiiiiiipppppppppppppaaa", "aa")
N1=faces.SequenceFace("aaaaaaaaaaaaaaaaaaaaaaaaiiiiiiiippppppNNNNNNNNaN", "aa")
N2=faces.SequenceFace("aaaaaaaaNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNaN", "aa")

string = 'aaaaaaaaaaaaaaaaaaaaaaaaiiiiiiiipppppppppppppaaa'

values = len (re.sub('[^a]','',string))*[1] + len (re.sub('[^i]','',string))*[0.5]+len (re.sub('[^p]','',string))*[2.2]

AH1 = faces.HistFace(values=values,header='bonjour'*30,mean=1)

AH1.aligned = -50

A1.aligned=True
A2.aligned=True

N1.aligned=False
N2.aligned=False
n = t.get_leaves()[-1]

flist= [A1,A2,N1,N2]
# Puedes pasar la lista de faces arriba o debajo del arbol cuando
# llamas a show().
t.show(ly, down_faces=[AH1,AH1])

#t.render('lolo.pdf',ly, down_faces=[AH1], up_faces=[AH1])
