#!/bin/bash
echo "Reading Params File...."

##
l=2
d=36
p=1
q[0]=0.5
q[1]=1.0
q[2]=2.0

input_graph=graph/dblp_snapgraph.txt
output_embedding_header=emb/dblp
final_embedding=emb/d32combined.txt