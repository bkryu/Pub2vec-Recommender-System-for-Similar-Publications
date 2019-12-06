# Pub2vec: A Recommender System for Similar Publications via Citation Network Embeddings
CS229 Fall 2019 Final Project
Last Updated 12/05/2019

Author: Brian K. Ryu

## Requirements
To run the entire code here including dataset processing, you will need Python2, Python3, [SNAP for Python](http://snap.stanford.edu/snappy/index.html), and the following libraries for Python: Numpy, Scipy, and JSON. 

To run using preprocessed data set and embeddings [(available here)](https://drive.google.com/drive/folders/1ZgqwtSXKe8toQkF8Y1QzcdsTCa9dBtJy?usp=sharing), you will need Python3 and the following libraries for Python: Numpy, Scipy, and JSON. 

## Steps to run
*Note: If you are using my preprocessed data, you can skip to step 3*

1. Download the DBLP v11 dataset from [Aminer](https://aminer.org/citation). Direct download link is here: [Link](https://lfs.aminer.cn/misc/dblp.v11.zip). Your file size should be approximately 4 GB and 12 GB before and after unzipping.

2. Run the following line:

```
./preprocess_DBLP.sh
```

This command should produce edgelists and maps that will be necessary to run pub2vec. 

3. Compile the node2vec code by running:

```
./compile_node2vec.sh
```

Ideally, your computer should be able to support openMP to speed up the embedding process.

4. Change directory into `./snap-master/examples/node2vec/graph` if you are not already there. Check that you have a `dblp_snapgraph.txt` in `./snap-master/examples/node2vec/graph` and five .json files in `./snap-master/examples/node2vec/`. If you downloaded my preprocessed data files, place them accordingly.

5. If you are creating your own embedding, run:

```
./pub2vec.sh params_DBLP.sh
```

This command runs pub2vec and aggregates the embedding file. At the end, you should have `d32combined.txt` in `./emb/`. If you donwloaded my preprocessed embedding, placed the `d32combined.txt` in `./emb/`.

6. Using Jupyter notebook, you can examine the iPython notebook I have written and ran in `Pub2vec_Analysis.ipynb` to query similar publications.