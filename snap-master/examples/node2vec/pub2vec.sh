#!/bin/bash
echo "Input parameter file is: $1"
source $1

echo "Executing node2vec..."

Outputs=""
for qvalue in "${q[@]}"
do
   : 
   ./node2vec -i:${input_graph} -o:${output_embedding_header}_l${l}_d${d}_p${p}_q${qvalue}.emb -l:$l -d:$d -p:$p -q:${qvalue} -dr -v
   Outputs="${Outputs} ${output_embedding_header}_l${l}_d${d}_p${p}_q${qvalue}.emb"
   # do whatever on $i
done

echo " "
echo "Done Executing node2vec"
echo "Now Aggregating Embeddings..."
echo " "
python3 ./ProcessEmbeddings.py ${output_embedding_header}_combined.emb ${Outputs}

echo "Embedding Processing Complete!"