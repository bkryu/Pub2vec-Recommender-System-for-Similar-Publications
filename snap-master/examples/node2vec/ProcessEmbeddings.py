import sys
import numpy as np


# Read embeddings
# print(sys.argv[1])

isFirst = True

for i in range(2, len(sys.argv)):
	# print(sys.argv[i])
	current_loaded = np.loadtxt(sys.argv[i], skiprows=1)
	current_loaded = current_loaded[np.argsort(current_loaded[:, 0])]
	if isFirst:
		toWrite = np.copy(current_loaded)

		isFirst = False
	else:
		toWrite = np.concatenate((toWrite, current_loaded), axis=1)

fmt_list = ['%1.4e']*toWrite.shape[1]
fmt_list[0] = '%d'

np.savetxt(sys.argv[1], toWrite, fmt=fmt_list)

'''
d32q05 = np.loadtxt('dblp_l3d32p1q1.emb', skiprows=1)
d32q1 = np.loadtxt('dblp_l3d32p1q05.emb', skiprows=1)
d32q2 = np.loadtxt('dblp_l3d32p1q2.emb', skiprows=1)
# d96q1 = np.loadtxt('dblp_l3d96p1q1.emb', skiprows=1)

# Sort by node index
d32q05 = d32q05[np.argsort(d32q05[:, 0])]
d32q1 = d32q1[np.argsort(d32q1[:, 0])]
d32q2 = d32q2[np.argsort(d32q2[:, 0])]
# d96q1 = d96q1[np.argsort(d96q1[:, 0])]

#Concatenate

d32_comb = (np.concatenate((d32q05, d32q1[:, 1:], d32q2[:, 1:]), axis=1))

fmt_list = ['%1.4e']*d32_comb.shape[1]
fmt_list[0] = '%d'

np.savetxt('d32combined.txt', d32_comb, fmt=fmt_list)
# np.savetxt('d96q1.txt', d96q1, fmt=fmt_list)
'''