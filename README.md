# Pub2vec: A Recommender System for Similar Publications via Citation Network Embeddings
Last Updated 12/05/2019

Author: Brian K. Ryu

## Abstract
Machine learning methods for recommender systems have proved their efficacy and have become popular for a wide range of applications ranging from product recommendations to advertisements and social networks. However, a potentially beneficial application of recommender systems that has yet to be realized is one for scientific publications. In this project, I present the pub2vec algorithm trained on a citation network to identify and recommend similar publications. A citation network is a social network that contains citation relations of academic publications. Although the network is simply a directed graph where nodes represent publications and edges represent citation relations, the network implicitly embodies information on the contents via links between citing and cited papers. The algorithm generates low-dimensional representations of a citation network, which are input to nearest neighbor algorithms to identify similar or closely related works. My results show that the publications recommended by pub2vec are highly relevant to queried publications. This work will potentially be able to aid researchers in conducting literature searches.

## tl;dr
Pub2vec constructs shallow graph embeddings of publications based on citation relations. These low-dimensional embeddings can be used to find similar publications.

![Overview](./Writeups/images/ColorOverview.pdf)

Some inputs and outputs of queries are shown below where titles highlighted red are *irrelevant* and titles highlighted blue are *relevant*

![Overview](./Writeups/images/Table.pdf)


*Note: This code base here was slightly modified from the high performance C++ SNAP library from the Stanford SNAP Group[1]*

## Requirements
To run the entire code here including dataset processing, you will need Python2, Python3, [SNAP for Python](http://snap.stanford.edu/snappy/index.html), and the following libraries for Python: Numpy, Scipy, and JSON. You will need Jupyter Notebook to see the iPython notebook using the embeddings.

To run using preprocessed data set and embeddings [(available here)](https://drive.google.com/drive/folders/1ZgqwtSXKe8toQkF8Y1QzcdsTCa9dBtJy?usp=sharing), you will need Python3 and the following libraries for Python: Numpy, Scipy, and JSON. You will need Jupyter Notebook to see the iPython notebook using the embeddings.

## Steps to run
*Note: If you are using my preprocessed data, you can skip to step 3 and skip most of 4 and 5 to generate embeddings.*

1. Download the DBLP v11 dataset from [Aminer](https://aminer.org/citation).[2] Direct download link is here: [Link](https://lfs.aminer.cn/misc/dblp.v11.zip). Your file size should be approximately 4 GB and 12 GB before and after unzipping.

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

*This project was comlpeted for CS229 Fall 2019 Final Project at Stanford University*

### References
[1] Leskovec, Jure, and Rok Sosič. "Snap: A general-purpose network analysis and graph-mining library." ACM Transactions on Intelligent Systems and Technology (TIST) 8.1 (2016): 1.

[2] Tang, Jie, et al. "Arnetminer: extraction and mining of academic social networks." Proceedings of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, 2008.