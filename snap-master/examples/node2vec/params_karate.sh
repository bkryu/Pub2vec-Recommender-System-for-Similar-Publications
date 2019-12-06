#!/bin/bash
echo "Reading Params File...."

##
l=3
d=24
p=1
q[0]=0.5
q[1]=1.0
q[2]=2.0


input_graph=graph/karate.edgelist
output_embedding_header=emb/karate
final_embedding=emb/karate_combined.emb