#!/bin/bash

echo "Preprocessing DBLP data into edgelist..."
python2 preprocess_DBLPsnap.py

echo " "

echo "Creating Maps Necessary for analysis..."
python3 create_maps.py

echo "Done preprocessing data!"

mv inv_id_map.json ./snap-master/examples/node2vec/
mv id_map.json ./snap-master/examples/node2vec/
mv fos_map.json ./snap-master/examples/node2vec/
mv name_map.json ./snap-master/examples/node2vec/
mv citation_map.json ./snap-master/examples/node2vec/
mv dblp_snapgraph.txt ./snap-master/examples/node2vec/graph/

cd ./snap-master/examples/node2vec